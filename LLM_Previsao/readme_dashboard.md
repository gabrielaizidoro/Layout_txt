# 📊 Previsão de Comissão com Modelos Estatísticos, LLM Local e Dashboard Interativo

Este projeto realiza uma análise preditiva do valor de **comissões de seguros** com base em dados históricos. A proposta visa explorar abordagens complementares entre modelos estatísticos tradicionais e modelos de linguagem (LLMs), além de disponibilizar os resultados em um dashboard interativo com Dash.

Utiliza:
- Modelos estatísticos clássicos (Regressão Linear, Random Forest)
- LLM local com **FLAN-T5** para gerar previsões em linguagem natural
- **Dash + Plotly** para visualização interativa

---

## 🧩 Estrutura do Projeto

```
├── input/                       # Arquivos Excel por mês (entrada)
├── output/                      # Arquivo com previsões e gráficos
│   ├── previsao_llm_30dias.xlsx
│   └── graficos/               # Gráficos por seguradora e produto
├── previsao_comissao.py         # Script principal
├── app_dashboard.py             # Dashboard interativo com Dash
├── requirements.txt             # Dependências do projeto
├── README.md                    # Este arquivo
```

---

## ⚙️ Instalação

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

### 1. Processar os dados e gerar previsões

```bash
python previsao_comissao.py
```

Esse script:
- Lê os arquivos Excel da pasta `input/`
- Treina modelos estatísticos e usa um LLM local para prever comissões
- Gera gráficos por seguradora e produto com histórico + previsão
- Exporta tudo em `output/previsao_llm_30dias.xlsx` e `output/graficos/`

### 2. Rodar o dashboard interativo

```bash
python app_dashboard.py
```

Acesse no navegador: [http://localhost:8050](http://localhost:8050)

Você poderá filtrar por seguradora e produto e visualizar as curvas de comissão (histórica e futura).

---

## 🔄 Expansões Sugeridas
- Agendamento com CRON ou Task Scheduler
- Envio automático por e-mail ou API
- Persistência dos dados com SQLite ou Parquet
- Deploy do dashboard via Docker ou Heroku

---

## 👩🏻‍💻 Autor
Gabriela Izidoro
