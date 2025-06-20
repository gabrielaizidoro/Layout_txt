import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

CAMINHO_EXCEL = os.getenv("CAMINHO_EXCEL")
CAMINHO_SAIDA = os.getenv("CAMINHO_SAIDA")
CAMINHO_ERROS = os.getenv("CAMINHO_ERROS")

tamanhos = {
    "Número da Apólice": 15,
    "Endosso": 0,
    "Tipo de Pessoa": 1,
    "CPF ou CNPJ": 18,
    "Ramo": 2,
    "Produto": 8,
}

tipos = {
    "Número da Apólice": "numerico",
    "Endosso": "numerico",
    "Tipo de Pessoa": "texto",
    "CPF ou CNPJ": "numerico",
    "Ramo": "numerico",
    "Produto": "numerico",
}

def formatar(valor, tam, tipo, campo):
    if pd.isna(valor): valor = ''
    valor = str(valor).strip()
    if tipo == 'numerico' and not valor.isdigit():
        raise ValueError(f"Campo '{campo}': '{valor}' deveria ser numérico.")
    if len(valor) > tam:
        raise ValueError(f"Campo '{campo}': '{valor}' excede {tam} caracteres.")
    return valor.zfill(tam) if tipo == 'numerico' else valor.ljust(tam)

df = pd.read_excel(CAMINHO_EXCEL).fillna('')
linhas_txt = []
erros = []

for i, row in df.iterrows():
    try:
        apolice_raw = str(row['Número da Apólice']).strip()
        endosso_raw = str(row['Endosso']).strip()

        apolice = formatar(apolice_raw, tamanhos["Número da Apólice"], tipos["Número da Apólice"], 'Número da Apólice')
        tipo_pessoa = formatar(row['Tipo de Pessoa'], tamanhos["Tipo de Pessoa"], tipos["Tipo de Pessoa"], 'Tipo de Pessoa')
        cpf_cnpj = formatar(row['CPF ou CNPJ'], tamanhos["CPF ou CNPJ"], tipos["CPF ou CNPJ"], 'CPF ou CNPJ')
        ramo = formatar(row['Ramo'], tamanhos["Ramo"], tipos["Ramo"], 'Ramo')
        produto = formatar(row['Produto'], tamanhos["Produto"], tipos["Produto"], 'Produto')

        proposta_raw = apolice_raw + endosso_raw if endosso_raw.isdigit() else apolice_raw
        proposta_fmt = formatar(proposta_raw, tamanhos["Número da Apólice"], 'numerico', 'Proposta (Apólice + Endosso)')

        linha = [
            "01", str(i + 1).zfill(12), "0000000", ramo, produto, proposta_fmt, apolice, tipo_pessoa,
            cpf_cnpj, "CLIENTE TESTE".ljust(50), "F", "19900101", "123456789".ljust(20), "1",
            "Rua Exemplo".ljust(50), "123".zfill(10), "Apto 1".ljust(20), "Bairro Central".ljust(30),
            "São Paulo".ljust(30), "SP", "01001000", "1", "11", "999999999".zfill(12),
            "   ", "    ", "          ", "0099", "".ljust(495)
        ]
        linhas_txt.append("".join(linha))
    except ValueError as e:
        erro_msg = f"Linha {i+2}: {str(e)}"
        erros.append(erro_msg)

with open(CAMINHO_SAIDA, 'w', encoding='utf-8') as f:
    f.write('\n'.join(linhas_txt))

if erros:
    with open(CAMINHO_ERROS, 'w', encoding='utf-8') as f:
        f.write('\n'.join(erros))
    print(f"{len(erros)} erro(s) encontrados. Detalhes em '{CAMINHO_ERROS}'.")
else:
    print(f"{len(linhas_txt)} linhas processadas com sucesso.")


