import datetime
import gspread
import streamlit as st
import pandas as pd
import numpy as np

credentials = {
    "type": "service_account",
    "project_id": "hwcollection",
    "private_key_id": "98c43b47b3718e490d5de0ce5c47c27435cff42a",
    "private_key": st.secrets["GS_TOKEN"],
    "client_email": "hw-873@hwcollection.iam.gserviceaccount.com",
    "client_id": "106471154499014422504",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/hw-873%40hwcollection.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

gc = gspread.service_account_from_dict(credentials)

sh = gc.open_by_key('1VLmAF5CrcEmMMAuDLN4z4YQ2XS4YYtBKMIVDKgtp1v4')

rd = sh.sheet1.get_all_records()

today = datetime.datetime.now().strftime("%Y-%m-%d")
today_week_day = datetime.datetime.now().strftime("%w")
today
monday = today - datetime.timedelta(days=3)
monday
df = pd.DataFrame(rd, columns = ['Kategoria','Kwota','Data','Uwagi','yyyymm'])

filtered_df_chart = df.loc[(df['Kategoria'] != "Dodaj")]

filtered_df_today = df.loc[(df['Data'] == today)]
filtered_df_today 

filtered_df_current_week = df.loc[(df['Data'] >= today) & (df['Data'] >= today)]

monthly_expenses = df.groupby([df['yyyymm'], 'Kategoria'])['Kwota'].sum().reset_index()
monthly_expenses_total = df.groupby([df['yyyymm']])['Kwota'].sum().reset_index()

monthly_expenses.loc[(df['Kategoria'] != "Dodaj")]
monthly_expenses_total.loc[(df['Kategoria'] != "Dodaj")]

#options_kat = set(df['Kategoria'])
#options_month = set(df['Month'])
#options_year = set(df['Year'])
#kat = st.multiselect("Kategoria",options_kat)
#mth = st.multiselect("Month",options_month)
#year = st.multiselect("Year",options_year)

st.line_chart(filtered_df_chart, x="Kategoria", y="Kwota", color="yyyymm")
