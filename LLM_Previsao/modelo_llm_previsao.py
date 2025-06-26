# Previsão de Comissão com Modelos Estatísticos e LLM Local

"""
Este script realiza análises preditivas de valor de comissão a partir de uma base fictícia de apólices,
utilizando modelos estatísticos (Regressão Linear e Random Forest) e uma LLM local com FLAN-T5.

Pré-requisitos:
- pip install pandas scikit-learn transformers torch openpyxl matplotlib

Etapas:
1. Carregamento e pré-processamento dos dados
2. Modelagem estatística com Regressão Linear e Random Forest
3. Geração de previsões com LLM local (google/flan-t5-base)
4. Análise preditiva por seguradora e produto para os próximos 30 dias
5. Geração de gráficos por seguradora e produto
"""

import pandas as pd
import numpy as np
import os
import time
import platform
import getpass
import sys
from datetime import timedelta, datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import matplotlib.pyplot as plt

# === Início da execução ===
inicio = time.time()
data_execucao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("\n🧑 Usuário: ", getpass.getuser())
print("💻 Máquina: ", platform.node())
print("🐍 Python:  ", sys.version.split()[0])
print("📅 Execução iniciada em:", data_execucao)
print("\n" + "="*50 + "\n")

# === Definir caminhos ===
caminho_input = "./input"
caminho_output = "./output"
caminho_graficos = os.path.join(caminho_output, "graficos")
os.makedirs(caminho_output, exist_ok=True)
os.makedirs(caminho_graficos, exist_ok=True)

# === (restante do código permanece igual até a parte de salvar o arquivo Excel) ===

print("✅ Previsões geradas. Salvando arquivo...")
df_resultados = pd.DataFrame(resultados)
output_path = os.path.join(caminho_output, "previsao_llm_30dias.xlsx")
df_resultados.to_excel(output_path, index=False)

# === 5. Geração de gráficos por Seguradora e Produto ===
print("📊 Gerando gráficos por Seguradora e Produto...")

for (seg, prod), grupo in df_resultados.groupby(["Seguradora", "Produto"]):
    historico = df[(df["Seguradora"] == seg) & (df["Produto"] == prod)]
    historico_grouped = historico.groupby("Data de Emissão")["Valor Comissão"].sum().reset_index()
    previsao_grouped = grupo.copy()
    previsao_grouped["Previsão Comissão"] = pd.to_numeric(previsao_grouped["Previsão Comissão"].str.replace("R$", "").str.replace(",", "."), errors='coerce')

    plt.figure(figsize=(10, 5))
    plt.plot(historico_grouped["Data de Emissão"], historico_grouped["Valor Comissão"], label="Histórico", marker="o")
    plt.plot(previsao_grouped["Data"], previsao_grouped["Previsão Comissão"], label="Previsão", linestyle="--", marker="x")
    plt.title(f"{seg} - {prod}")
    plt.xlabel("Data")
    plt.ylabel("Comissão (R$)")
    plt.legend()
    plt.tight_layout()
    nome_arquivo = f"{seg}_{prod}.png".replace(" ", "_")
    plt.savefig(os.path.join(caminho_graficos, nome_arquivo))
    plt.close()

# === Finalização ===
print("\n✅ PROCESSAMENTO CONCLUÍDO")
print(f"📁 Arquivo gerado: {output_path}")
print("📊 Gráficos salvos em:", caminho_graficos)
print("⏱️ Tempo total de execução: {:.2f} segundos".format(time.time() - inicio))
