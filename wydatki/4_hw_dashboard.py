from datetime import datetime, timedelta
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

sh = gc.open_by_key('1yi769GiV0MsO2hHCJHhQJaIL96_3wu955LZxo79hOkU')

rd = sh.sheet1.get_all_records()

df = pd.DataFrame(rd, columns = ['id','marka'])

st.write("Dzisiejsze wydatki")

monthly_expenses = df.groupby([df['marka']])['marka'].count()

monthly_expenses.sort_values(by='marka',ascending=False)
