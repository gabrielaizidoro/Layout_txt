# Verificador de Envio de Arquivos - Seguradoras 📦

Este projeto automatiza a verificação de arquivos enviados , conferindo se os arquivos foram recebidos corretamente em cada dia útil do mês atual.

Um rascunho de e-mail é gerado com um dashboard que resume, por seguradora e por data, se o envio ocorreu ou não.

---

## ✅ Funcionalidades

- Verifica arquivos com nome no padrão: `ARQEMISS_<SEGURADORA>_*.txt`
- Identifica o envio em cada dia útil do mês até a data atual
- Gera uma tabela com:
  - Seguradoras nas linhas
  - Dias úteis como colunas
  - Status: ✅ Enviado ou ❌ Não enviado
- Cria um rascunho de e-mail via Outlook com o dashboard embutido em HTML

---

## 🧱 Estrutura

```
verificador_envio_arquivos/
├── README.md
├── requirements.txt
└── verificador_arquivos/
    └── main.py         # Script principal

```

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- Microsoft Outlook instalado (necessário para criação de e-mail)
- Pacotes Python:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como usar

1. **Ajuste o caminho da pasta de rede**  
   No arquivo `main.py`, modifique a variável `diretorio` com o caminho onde os arquivos são salvos.

2. **Rode o script**

```bash
python boletim_automatico/main.py
```

3. **Valide o e-mail gerado**  
   Um rascunho será aberto no Outlook com o dashboard pronto para envio manual.

---

## 🛠️ Personalizações sugeridas

- Adicionar novas seguradoras no dicionário `padroes_arquivos`
- Exportar o relatório também para Excel ou salvar como `.html`
- Agendar a execução via Agendador de Tarefas do Windows

---

Feito com 💼 para simplificar atividades manuais.

## 👩‍💻 Autor

Desenvolvido por **Gabriela Izidoro**  
Especialista em Dados, Automação e Processos Contábeis
