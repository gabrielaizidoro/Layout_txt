import os
import pandas as pd
from datetime import datetime

# Solicita diretório de entrada e saída do usuário
#Digite o caminho completo da pasta com os arquivos .txt
DIRETORIO = r"INSIRA AQUI O CAMINHO DO DIRETÓRIO COM OS ARQUIVOS"

#Digite o caminho completo da pasta onde deseja salvar o relatório:
PASTA_SAIDA = r"INSIRA AQUI O CAMINHO DO DIRETÓRIO COM OS ARQUIVOS"

# Cria pasta de saída, se não existir
os.makedirs(PASTA_SAIDA, exist_ok=True)

# Lista para armazenar os resultados da validação
resultados = []

# Função para validar se uma string é numérica
def is_numeric(s):
    return s.isdigit()

# Função para validar data no formato yyyymmdd
def is_valid_date(s):
    try:
        datetime.strptime(s, "%Y%m%d")
        return True
    except ValueError:
        return False

# Percorrer todos os arquivos .txt ou .TXT no diretório
for nome_arquivo in os.listdir(DIRETORIO):
    if nome_arquivo.lower().endswith(".txt") and \
       (nome_arquivo.upper().startswith("ARQEMISS") or nome_arquivo.upper().startswith("EMI")):

        caminho_arquivo = os.path.join(DIRETORIO, nome_arquivo)

        if os.path.getsize(caminho_arquivo) <= 2048:
            continue  # pular arquivos menores ou iguais a 2KB

        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
            for idx, linha in enumerate(linhas, start=1):
                linha = linha.rstrip('\n')
                if len(linha) != 20:
                    resultados.append({
                        'Arquivo': nome_arquivo,
                        'Linha': idx,
                        'Campo': 'Tamanho da Linha',
                        'Valor': f'{len(linha)} caracteres',
                        'Status': 'ERRO'
                    })
                    continue

                prefixo = linha[:2]

                if prefixo == '03':
                    endosso = linha[2:7]
                    apolice = linha[7:15]

                    resultados.append({
                        'Arquivo': nome_arquivo,
                        'Linha': idx,
                        'Campo': 'Número do Endosso (03)',
                        'Valor': endosso,
                        'Status': 'OK' if is_numeric(endosso) else 'ERRO'
                    })

                    resultados.append({
                        'Arquivo': nome_arquivo,
                        'Linha': idx,
                        'Campo': 'Número da Apólice (03)',
                        'Valor': apolice,
                        'Status': 'OK' if is_numeric(apolice) else 'ERRO'
                    })

                elif prefixo == '02':
                    apolice = linha[2:7]
                    data_emissao = linha[7:15]

                    resultados.append({
                        'Arquivo': nome_arquivo,
                        'Linha': idx,
                        'Campo': 'Número da Apólice (02)',
                        'Valor': apolice,
                        'Status': 'OK' if is_numeric(apolice) else 'ERRO'
                    })

                    resultados.append({
                        'Arquivo': nome_arquivo,
                        'Linha': idx,
                        'Campo': 'Data de Emissão (02)',
                        'Valor': data_emissao,
                        'Status': 'OK' if is_valid_date(data_emissao) else 'ERRO'
                    })

# Criar DataFrame e exportar para Excel
df_resultados = pd.DataFrame(resultados)
caminho_saida = os.path.join(PASTA_SAIDA, "relatorio_validacao.xlsx")
df_resultados.to_excel(caminho_saida, index=False)

print(f"Validação concluída. Relatório salvo em: {caminho_saida}")
