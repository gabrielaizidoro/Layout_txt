"""
Script para extrair linhas específicas de arquivos .txt posicionais com base em identificadores contidos em uma planilha Excel.

Funcionalidades:
- Lê uma planilha contendo chaves de referência, apólice e endosso.
- Filtra linhas de arquivos .txt posicionais que contenham essas chaves em posição fixa.
- Gera dois arquivos: um com as linhas encontradas e outro com as chaves não localizadas.
- Ordena a saída pelas duas primeiras posições da linha.
- Exibe um resumo da execução com tempo, status e ambiente.

Autor: Gabriela Izidoro
Data: 2025-06-19
Versão: 1.3
"""
#update
import os
import pandas as pd
import glob
from datetime import datetime
import time
import getpass
import platform
import sys
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Pegar caminhos do arquivo .env
CAMINHO_PLANILHA = os.getenv("CAMINHO_PLANILHA")
COLUNA_CHAVE = os.getenv("COLUNA_CHAVE")
PASTA_TXT = os.getenv("PASTA_TXT")
PASTA_SAIDA = os.getenv("PASTA_SAIDA")

# === FUNÇÕES AUXILIARES ===

def carregar_planilha_completa(caminho_arquivo, coluna_chave):
    """
    Lê a planilha contendo as chaves, apólices e endossos.

    Args:
        caminho_arquivo (str): Caminho para o arquivo Excel.
        coluna_chave (str): Nome da coluna que contém a chave de referência.

    Returns:
        pd.DataFrame: DataFrame com a planilha limpa e colunas como string.
    """
    df = pd.read_excel(caminho_arquivo, dtype=str)
    df = df.fillna("")
    df[coluna_chave] = df[coluna_chave].str.strip()
    return df

def processar_arquivos_txt(pasta, ids_referencia):
    """
    Processa todos os arquivos .txt da pasta, filtrando linhas com chaves de referência nas posições 3 a 15.

    Args:
        pasta (str): Caminho da pasta com arquivos .txt.
        ids_referencia (set): Conjunto de chaves a serem localizadas.

    Returns:
        tuple: (lista de tuplas (chave, linha), conjunto de chaves encontradas)
    """
    linhas_encontradas = []
    encontrados = set()
    arquivos_txt = glob.glob(os.path.join(pasta, "*.txt"))

    for caminho_arquivo in arquivos_txt:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            for linha in f:
                if len(linha) >= 56:
                    trecho = linha[2:15].strip()
                    if trecho in ids_referencia:
                        linhas_encontradas.append((trecho, linha))
                        encontrados.add(trecho)
    return linhas_encontradas, encontrados

def salvar_linhas_em_arquivo(linhas, pasta_saida):
    """
    Salva as linhas encontradas em um arquivo .txt, ordenadas pelos dois primeiros caracteres da linha.

    Args:
        linhas (list): Lista de tuplas (chave, linha completa).
        pasta_saida (str): Caminho da pasta onde salvar o arquivo.

    Returns:
        str: Caminho completo do arquivo salvo.
    """
    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"ARQEMISS_CIA_Encontrado_{data_hora}.txt"
    caminho_completo = os.path.join(pasta_saida, nome_arquivo)

    linhas_ordenadas = sorted(linhas, key=lambda x: x[1][0:2])

    with open(caminho_completo, "w", encoding="utf-8") as f:
        for _, linha in linhas_ordenadas:
            f.write(linha)

    return caminho_completo

def salvar_nao_encontrados(df_planilha, ids_encontrados, pasta_saida):
    """
    Gera um arquivo com as chaves da planilha que não foram encontradas nos arquivos .txt.

    Args:
        df_planilha (pd.DataFrame): Planilha original com as colunas "Chave do arquivo", "Apólice", "Endosso".
        ids_encontrados (set): Chaves que foram efetivamente localizadas nos arquivos.
        pasta_saida (str): Pasta onde o relatório será salvo.

    Returns:
        tuple: (caminho do arquivo salvo ou None, número de chaves não encontradas)
    """
    faltantes_df = df_planilha[~df_planilha[COLUNA_CHAVE].isin(ids_encontrados)]

    if faltantes_df.empty:
        return None, 0

    data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"Nao_encontrados_{data_hora}.txt"
    caminho_completo = os.path.join(pasta_saida, nome_arquivo)

    with open(caminho_completo, "w", encoding="utf-8") as f:
        f.write("Chave do Arquivo\tApólice\tEndosso\n")
        for _, row in faltantes_df.iterrows():
            chave = row.get("Chave do arquivo", "N/A").strip()
            apolice = row.get("Apólice", "N/A").strip()
            endosso = row.get("Endosso", "N/A").strip()
            f.write(f"{chave}\t{apolice}\t{endosso}\n")

    return caminho_completo, len(faltantes_df)

# === EXECUÇÃO PRINCIPAL ===
if __name__ == "__main__":
    inicio = time.time()
    data_execucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n🧑 Usuário: ", getpass.getuser())
    print("💻 Máquina: ", platform.node())
    print("🐍 Python:  ", sys.version.split()[0])
    print("\n" + "="*50)
    
    # === PRINT FINAL ===
    print("✅ PROCESSAMENTO CONCLUÍDO\n")
    print("🔍 Carregando planilha de referência...")
    df_planilha = carregar_planilha_completa(CAMINHO_PLANILHA, COLUNA_CHAVE)
    ids = set(df_planilha[COLUNA_CHAVE])
    total_ids = len(ids)

    print(f"📂 {total_ids} chaves carregadas da planilha.")

    print("\n🛠️  Processando arquivos .txt...\n")
    linhas_filtradas, encontrados = processar_arquivos_txt(PASTA_TXT, ids)
    total_encontradas = len(encontrados)

    caminho_saida = salvar_linhas_em_arquivo(linhas_filtradas, PASTA_SAIDA)
    caminho_nao_encontrados, total_nao_encontrados = salvar_nao_encontrados(df_planilha, encontrados, PASTA_SAIDA)

    fim = time.time()
    duracao = round(fim - inicio, 2)
  
    print(f"📅 Data/Hora de execução: {data_execucao}")
    print(f"🕒 Tempo total: {duracao} segundos\n")

    print(f"📊 Resumo:")
    print(f"   - Total de chaves na planilha:     {total_ids}")
    print(f"   - Chaves encontradas nos .txt:     {total_encontradas}")
    print(f"   - Chaves não encontradas:          {total_nao_encontrados}\n")

    print("📄 Arquivos gerados:")
    print(f"   - Emissões filtradas:                {caminho_saida}")
    if caminho_nao_encontrados:
        print(f"   - Relatório de erros:              {caminho_nao_encontrados}")
    else:
        print(f"   - Relatório de erros:              (nenhum erro encontrado)")

    print("\n✅ STATUS:", "Finalizado com alertas" if total_nao_encontrados else "Finalizado com sucesso")
    print("="*50 + "\n")
