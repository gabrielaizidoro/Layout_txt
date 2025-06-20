
# 🧾 Criação de Arquivo TXT Posicional para Emissões (Cria EMI)

Este projeto gera automaticamente um **arquivo `.txt` posicional** a partir de um modelo Excel com dados de apólice, cliente e produto. Ele é útil para criar layouts padrão de emissão de seguros, como arquivos `ARQEMISS.txt`.

---

## 🚀 Funcionalidades

- 📥 Lê um Excel com dados de apólice, CPF/CNPJ, ramo, produto e outros campos
- 📏 Valida os tamanhos e tipos de cada campo (texto ou numérico)
- 🧠 Formata os campos conforme layout posicional esperado
- 🧾 Gera um `.txt` com todas as linhas posicionais corretamente montadas
- ⚠️ Cria um relatório de erros (`.txt`) com as linhas que não passaram na validação

---

## 📁 Estrutura de Diretórios

Cria EMI/

```
├── Input/
│   └── modelo_dados_usuario_ajustado.xlsx  # Planilha com os dados de entrada
├── Output/
│   ├── ARQEMISS.txt                        # Arquivo gerado posicionalmente
│   └── erros_validacao.txt                 # Log com os erros encontrados (se houver)
├── Main.py                                 # Script principal
├── .env                                    # Configurações de caminho (não versionado)
├── requirements.txt                        # Pacotes utilizados
└── README.md                               # Este documento
```

---

## 📑 Estrutura esperada da planilha (`modelo_dados_usuario_ajustado.xlsx`)

| Número da Apólice | Endosso | Tipo de Pessoa | CPF ou CNPJ | Ramo | Produto |
|-------------------|---------|----------------|-------------|------|---------|
| 123456789012345   | 001     | F              | 12345678900 | 01   | 0099    |

- **Todos os campos são obrigatórios**
- **Tipo de Pessoa** deve ser texto
- **Demais campos** são numéricos (valida se têm apenas dígitos)
- Os tamanhos são fixos e padronizados (ex: Apólice = 15 caracteres)

---

## ⚙️ Variáveis de Ambiente (.env)

Este projeto usa um arquivo `.env` para guardar os caminhos dos arquivos:

```
CAMINHO_EXCEL=Input/modelo_dados_usuario_ajustado.xlsx
CAMINHO_SAIDA=Output/ARQEMISS.txt
CAMINHO_ERROS=Output/erros_validacao.txt
```

⚠️ O arquivo `.env` não é enviado ao GitHub (está no `.gitignore`)

---

## ▶️ Como Executar

1. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Ajuste o arquivo `.env` com os caminhos corretos

4. Execute o script:
   ```bash
   python Main.py
   ```

---

## 📌 Saída Esperada

### ✅ No terminal:
```
10 linhas processadas com sucesso.
```
Ou, em caso de erros:
```
2 erro(s) encontrados. Detalhes em 'Output/erros_validacao.txt'.
```

### 📄 Arquivo gerado:
- `ARQEMISS.txt` com linhas posicionais conforme layout
- `erros_validacao.txt` com mensagens como:
  ```
  Linha 4: Campo 'CPF ou CNPJ': 'ABC123' deveria ser numérico.
  ```

---

## 🧠 Notas Técnicas

- O layout segue formatação posicional com validação de tipo e tamanho
- A formatação e validação são centralizadas na função `formatar()`
- O código pode ser facilmente adaptado para novos layouts

---

## 👩‍💻 Autor

Desenvolvido por **Gabriela Izidoro**  
Especialista em Dados, Automação e Processos Contábeis
