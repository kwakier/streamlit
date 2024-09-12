import gspread
import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

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

sh = gc.open_by_key('1yi769GiV0MsO2hHCJHhQJaIL96_3wu955LZxo79hOkU')

rd = sh.sheet1.get_all_records()

df = pd.DataFrame(rd, columns = ['id','year','quantity','marka'])
dfl = df['id'].str.lower().str[0:5]

def cnt():
    #cnt = sum(df['quantity'])
    cnt = int(len(set(df['id'])))
    #cnt = int(len(df['id']))
    return cnt
cnt()

st.write(f"Mamy **{cnt()}** samochodzików")
ti = st.text_input(label='szukaj')
til = ti.lower()

if ti:
    if til in dfl.values: 
        st.write("Mamy go") 
        st.write(df.loc[df['id'].str.lower().str[0:5] == til ])
    else:
        st.write("Kupujemy!")
        ro = st.text_input(label='rocznik')
        options = set(df['marka'])
        ma = st.selectbox("marka",options)
        if ma == "Dodaj":
            dodmar = st.text_input("Nowa marka")
        else:
            dodmar = ma
        dodaj_hw = st.button("Dodaj")
        if dodaj_hw:
            sh.sheet1.update_cell(cnt()+2,1, ti)
            sh.sheet1.update_cell(cnt()+2,2, int(ro))
            sh.sheet1.update_cell(cnt()+2,5, dodmar)
           
else:
    st.write("Sprawdźmy")

refresh = st.button("Odswiez")
if refresh:
    cnt()

##dfy = df['year']
#dfy = filter(None,df['year'])

#cl = Counter(dfy).keys() # equals to list(set(words))
#cv = Counter(dfy).values() # counts the elements' frequency

##cl = Counter(dfy)

##cldf = pd.DataFrame.from_dict(cl, orient='index').reset_index()
#cldf

#df
