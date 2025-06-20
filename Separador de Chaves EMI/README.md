# 📄 Separador de Emissões por Chave de Arquivo (TXT Posicional + Planilha Excel)

Este projeto automatiza a extração de linhas específicas de arquivos `.txt` posicionais, com base em **identificadores definidos em uma planilha Excel**. Ele é ideal para processar registros de emissão, endosso ou faturas com estrutura fixa.

---

## 🚀 Funcionalidades

- 📥 Lê uma planilha com colunas: **Chave do Arquivo**, **Apólice** e **Endosso**
- 🔍 Lê arquivos `.txt` posicionais
- 🧠 Filtra linhas que contenham a chave da planilha nas posições **3 a 15** do `.txt`
- 📊 Ordena as linhas encontradas com base nos **dois primeiros caracteres da linha**
- 📄 Gera dois arquivos:
  - Um com as linhas filtradas
  - Um com as chaves **não encontradas**, incluindo apólice e endosso
- 🧾 Exibe **resumo profissional da execução** no terminal: tempo, status, caminho dos arquivos, ambiente, etc.

---

## 📁 Estrutura de Diretórios

SeparadorEmissao/

- ├── Input/
- │ ├── Referencias.xlsx # Planilha com as chaves e dados
- │ └── ARQEMISS_.txt # Arquivos posicionais de entrada
- ├── Output/
- │ ├── Arqemiss_filtrados_.txt # Saída com emissões encontradas
- │ └── Nao_encontrados_*.txt # Saída com chaves não encontradas
- ├── Main.py # Script principal do projeto
- ├── venv # ambiente virtual
- ├── requirements.txt # biblioteca de versões do projeto
- └── README.md # Este arquivo

---

## 📑 Estrutura esperada da planilha (`Referencias.xlsx`)

A planilha deve conter no mínimo:

| Chave do arquivo | Apólice         | Endosso         |
|------------------|------------------|------------------|
| 000000000010     | 123 | 456 |
| 000000000020     | 456 | 789 |

- Os valores devem estar **como texto** no Excel (para manter zeros à esquerda, se houver)
- A chave é comparada com o trecho fixo do `.txt` nas posições **3 a 15**

---

## ▶️ Como Executar

1. Certifique-se de ter Python 3.7+
2. Instale os pacotes (caso necessário):

- pip install (pandas, openpyxl)

3. Certifique que ajustou o caminho das pastas `(para a sua máquina)`:

- Input
- Output

4. Coloque os arquivos na pasta Input/:

- A planilha Referencias.xlsx

- Os arquivos .txt posicionais

5. Execute o script:

- python separador.py

---

## 📌 Saída Esperada
O terminal exibe algo como:

✅ PROCESSAMENTO CONCLUÍDO

📅 Data/Hora de execução: 
🕒 Tempo total: 

📊 Resumo:
   - Total de chaves na planilha:     
   - Chaves encontradas nos .txt:     
   - Chaves não encontradas:           

📄 Arquivos gerados:
   - Linhas filtradas:                
   - Relatório de erros:              

🧑 Usuário:  
💻 Máquina:  
🐍 Python:   

✅ STATUS: Finalizado com alertas/sem alertas

## 🧠 Notas Técnicas
A posição 3 a 15 (do layout congeneres) equivale a linha[2:15] em Python

Apenas linhas com mínimo 56 caracteres são consideradas

O script está modularizado para fácil manutenção ou integração com pipelines

## 👩‍💻 Autor
Desenvolvido por Gabriela Izidoro

Analista de Dados e Automação