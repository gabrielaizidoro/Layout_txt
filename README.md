
# 📦 Layout_txt — Repositório de Projetos para Geração e Validação de Arquivos Posicionais

Este repositório centraliza projetos Python voltados à **automação de layouts posicionais em .txt**, muito utilizados em contextos como seguros, emissões e validações contábeis.

---

## 📁 Projetos Incluídos

### 1. **🔍 Separador de Chaves EMI**
> Extração de linhas específicas de arquivos `.txt` com base em chaves de referência definidas em uma planilha Excel.

- 📥 Lê vários arquivos `.txt` em um diretório
- 🔎 Procura pelas chaves na posição 3 a 15 de cada linha
- 📊 Compara com as chaves de uma planilha `.xlsx`
- ✅ Gera um novo `.txt` com as linhas encontradas
- ⚠️ Cria um relatório com chaves não localizadas

📂 Pasta: `Separador de Chaves EMI`  
📄 [README completo](./Separador%20de%20Chaves%20EMI/README.md)

---

### 2. **🧾 Cria EMI — Gerador de Arquivo TXT Posicional**
> Gera automaticamente arquivos `.txt` posicionais com base em uma planilha de dados de apólice e produto.

- 🧠 Faz validação por tipo e tamanho de campo
- 🧮 Formata dados em estrutura fixa
- 📄 Exporta para `ARQEMISS.txt` com layout padrão
- ⚠️ Gera relatório de erros por linha inválida

📂 Pasta: `Cria EMI`  
📄 [README completo](./Cria%20EMI/README.md)

---

## 🛠️ Requisitos

- Python 3.8+
- Uso recomendado com `venv`
- Instalação de dependências via `requirements.txt` em cada projeto

---

## 🧪 Execução

Cada projeto contém seu próprio `README.md` com instruções completas para:

- Ativação do ambiente virtual
- Configuração do `.env`
- Execução do script principal

---

## 👩‍💻 Autora

**Gabriela Izidoro**  
Automação • Dados • Processos Contábeis  
[github.com/gabrielaizidoro](https://github.com/gabrielaizidoro)

---
