import os
import glob
import datetime
import pandas as pd
import locale
from win32com.client import Dispatch

# === CONFIGURAÇÕES ===
diretorio = r"\\caminho\da\pasta\compartilhada"  # Altere para seu caminho real
padroes_arquivos = {
    "Seguradora 1": "ARQEMISS_Seguradora1_*.txt",
    "Seguradora 2": "ARQEMISS_Seguradora2_*.txt"
}

# Define a localidade para português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# === DATAS DO MÊS ATÉ ONTEM ===
hoje = datetime.date.today()
ontem = hoje - datetime.timedelta(days=1)
inicio_mes = hoje.replace(day=1)
dias_ate_ontem = [inicio_mes + datetime.timedelta(days=i) for i in range((ontem - inicio_mes).days + 1)]
dias_uteis = [d.date() for d in pd.bdate_range(start=inicio_mes, end=ontem)]

# === VERIFICAÇÃO POR SEGURADORA E DIA ===
dados = {}
debug_info = {}

for seguradora, padrao in padroes_arquivos.items():
    arquivos = glob.glob(os.path.join(diretorio, padrao))
    datas_arquivos = [datetime.date.fromtimestamp(os.path.getmtime(arq)) for arq in arquivos]
    debug_info[seguradora] = datas_arquivos
    status_por_dia = []

    for dia in dias_ate_ontem:
        enviado = dia in datas_arquivos
        if enviado:
            status_por_dia.append("✅")
        elif dia in dias_uteis:
            status_por_dia.append("❌")
        else:
            status_por_dia.append('<span style="color:gray">🛈</span>')  # dia não útil e sem envio

    dados[seguradora] = status_por_dia

# === DEBUG OPCIONAL ===
print("=== Datas de modificação por seguradora ===")
for seg, datas in debug_info.items():
    print(f"{seg}: {[d.strftime('%d/%m/%Y') for d in datas]}")

# === CRIAÇÃO DA TABELA ===
colunas = [data.strftime('%d/%m') for data in dias_ate_ontem]
df_dash = pd.DataFrame(dados, index=colunas).T
df_dash.index.name = "Seguradora"
html_table = df_dash.to_html(escape=False)

# === LEGENDA ===
legenda = """
<p><b>Legenda:</b></p>
<ul>
<li>✅ Arquivo encontrado no dia.</li>
<li>❌ Arquivo não encontrado em dia útil.</li>
<li>🛈 Arquivo não encontrado em dia não útil.</li>
</ul>
"""

# === RASCUNHO DE EMAIL NO OUTLOOK ===
outlook = Dispatch("Outlook.Application")
mail = outlook.CreateItem(0)

mail.To = "insira_o_email@gmail.com"
mail.Subject = f"BOLETIM DE EMISSÕES DO COL - {hoje.strftime('%d/%m/%Y')}"
mail.HTMLBody = f"""
<p>Olá,</p>
<p>Segue abaixo o status acumulado de envio dos arquivos das seguradoras do COL, referente ao mês de <b>{hoje.strftime('%B/%Y')}</b>:</p>
{html_table}
{legenda}
<p>Atenciosamente,<br><b>Fulano de tal</b></p>
"""

mail.Display()