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

df = pd.DataFrame(rd, columns = ['id','Kategoria','Kwota','Data','Uwagi'])

def cnt():
    cnt = int(len(set(df['id'])))
    return cnt
cnt()

today = datetime.datetime.now().strftime('%Y-%m-%d')
options = set(df['Kategoria'])
kat = st.selectbox("Kategoria",options)
kwo = st.number_input(label='Kwota')
uwa = st.text_input(label='Uwagi')
if kat == "Dodaj":
    dodkat = st.text_input("Nowa kategoria")
else:
    dodkat = kat
dodaj = st.button("Dodaj")
refresh = st.button("Odswiez")
if refresh:
    cnt()
if dodaj:
    sh.sheet1.update_cell(cnt()+2,1, cnt()+1)
    sh.sheet1.update_cell(cnt()+2,2, dodkat)
    sh.sheet1.update_cell(cnt()+2,3, kwo)
    sh.sheet1.update_cell(cnt()+2,4, today)
    sh.sheet1.update_cell(cnt()+2,5, uwa)
