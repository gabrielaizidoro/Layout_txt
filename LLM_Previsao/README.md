# 📊 Previsão de Comissão com Modelos Estatísticos e LLM Local

Este projeto realiza uma análise preditiva do valor de **comissões de seguros** com base em dados históricos. A proposta visa explorar abordagens complementares entre modelos estatísticos tradicionais e modelos de linguagem (LLMs), possibilitando previsões a partir de dados estruturados e descrições em linguagem natural.

Utiliza:

- Modelos estatísticos clássicos (Regressão Linear, Random Forest) para estabelecer linhas de base e interpretar relações entre variáveis numéricas e categóricas
- LLM local com **FLAN-T5** para simular previsões em linguagem natural, permitindo geração de respostas descritivas e exploratórias

---

## 🧩 Estrutura do Projeto

```
├── input/               # Arquivos Excel por mês (entrada)
├── output/              # Arquivo gerado com previsões futuras
├── previsao_comissao.py # Script principal
├── README.md            # Este arquivo
```

---

## ⚙️ Requisitos

```bash
pip install pandas scikit-learn transformers torch openpyxl
```

---

## 🚀 Como usar

1. Coloque seus arquivos Excel (um por mês) na pasta `input/`
2. Execute o script principal:

```bash
python previsao_comissao.py
```

O script:

- Lê a aba com mais dados de cada planilha (evitando abas com tabelas dinâmicas ou vazias)
- Realiza pré-processamento dos dados estruturados
- Aplica modelos estatísticos para prever a comissão com base em variáveis como seguradora, produto, prêmio e data
- Utiliza LLM local para simular previsões com linguagem natural, gerando insights e respostas automatizadas
- Salva previsões dos próximos 30 dias por seguradora e produto em um arquivo Excel

---

## 📊 Sobre os Modelos Utilizados

### Modelos Estatísticos

- **Regressão Linear**: utilizado como baseline pela sua simplicidade e interpretabilidade
- **Random Forest Regressor**: escolhido pela capacidade de capturar relações não-lineares e interações entre variáveis sem necessidade de normalização

Estes modelos permitem mensurar o desempenho com métricas como MAE (erro absoluto médio), RMSE (raiz do erro quadrático médio) e R² (coeficiente de determinação), servindo como referência para comparar com as abordagens de LLM.

### LLM - Modelo de Linguagem

- Utiliza o modelo **FLAN-T5** local para gerar respostas textuais a partir de prompts descritivos, simulando cenários de previsão e auxiliando em tomadas de decisão exploratórias.
- Essa abordagem é útil para aplicações que exigem geração de explicações, relatórios automatizados ou sistemas interativos baseados em linguagem.

---

## 🔄 Expansões Sugeridas

- Substituir FLAN-T5 por um modelo finetuned ou treinado com contexto do negócio
- Adaptar para servir via API (FastAPI) ou interface (Streamlit)
- Incluir validação cruzada, grid search ou SHAP para interpretabilidade
- Agendamento automatizado com log de execução

---

## 👩🏻‍💻 Autor

Gabriela Izidoro

