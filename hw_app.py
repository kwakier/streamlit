import gspread
import streamlit as st
import pandas as pd

credentials = {
    "type": "service_account",
    "project_id": "hwcollection",
    "private_key_id": "98c43b47b3718e490d5de0ce5c47c27435cff42a",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDHM/x6ReGxWnje\nsu+adViHXd6xtiphwQPi0VlDy0DdCz8Swxyzm6XzMSZ5DhTTchE7O2sXdl3Yd+bq\nhPD+7qA0I5l9OJLsAtkELlOz53ffqY8tsjUF5tCb8bjbhqcuT1J6sk7xTFQgPfKf\nASh2+LbALDBhsxJ1bYnw1lW5UJeYFL4kop77bIURTRBXvRMgyJ0pF0SFiMV35vbO\nFsXQVzNH6/d4j3Qrf189E7vsS7VOlyfIdUmcX+Zxag/SqHD07ghIiRKQqredn6LE\nwB4770dYNP5Ek7ua3Ecp2lMjzAWAQCNDbaOa2lnKdhLedE4r9ibvbQeNR0ohQZ89\njYlsRBNtAgMBAAECggEAA0O01YQjqLZk2LFx/8QAiWdeaOclVqjFGYh4wAWqsHSo\nufP8mmzokU2y5bT3Xme2JJRasu27p/p/DETVdjgO5AvZThYJQljhmZHwyTf33PB4\najVLbSdVL9kMQHy6bKXcIiqd5JJtpoGdYkGwmhKFXCzdNhyrJsV+xzWb/gd2FIXr\nFSJqWbJu/zvWGC+7cw6nkr7YKjqx5KdP4mCpGE6EQ6pUlqQZKacc0wYU5TWLuoXh\ndOlCFOrS49A5qmfmg2XQmxv0XMD8voU4YCjkMbJ8yoJlpisIIR9oiDEtm/Pnqoer\nhYFDuLFKo3O7Sl3ODt4r4gcJeD6ArC9oLeX6eZLKAQKBgQDwtT64VT9/8gOJLSvH\n3ntQTJm9EpQD8GRYUbK2adocSsUlsTVyhXVmJCHVl/lJ5/z455iJltgvRSs6aFiP\nxC/tvar2G3+1kJXwMZtOLSWxaFmbLLLjuDpcOqoHe7ztHO9nDsNn528wbfPF/SfE\nv7Fvuu8LK3sONzLEt3Eqj/ehwQKBgQDT27nVddcLZh7IeMqWZJnm/FTKaTd3yurk\no1osugH1ky1u3ZgG863aE/Y1omY35fr2b7VsE52w0tUgHDujYj5XV7mHjSi+eUMq\n2025/Px6hrHf3CAtLoqj/3df4s/IMeT7znWAW+/ZkkpYxldmdjmSczNCoa9phAU7\ndtFvpxTErQKBgF8TV+i7U0+YKilevDJAAHkhKIBz/B7qLthrvKksekg+iExxCGlp\nqYtkrjCNzJuSlGtEHw4JlO5m5cI2QPTYSw4eoo5/Ihx3NaIgFfX1AzRlwS73otkr\nhXG0gkBecas+iJkuTaSW12ZLp8QGUFT4Wn+FWLISxJJC3zywMHTdVLSBAoGAczfa\ndybhTwe40hovQ19u+9pbWsGiMvoeiT31usFmc2IZoWPOXGmGMUYN7tllch0XQZM7\nPY3lgtcGpbH1FURG10WUVw4EDKLyTop6WR4nSZObhT24GhpnuA0lpPY7Pos0F2YP\nLUHSzabr3B/yRH0jjmwsgp5gQahVGCPkfy6E8vkCgYEAkPb1CU1xwTAXUUXWcpTx\nW/jLxEHKEmmmPZ/PToFKGdjNXLexyf0FS2JMWq6sDgofw4+X/gt5ddDX6hoPqRii\nb3Ao4Y0oBNr11EPpyo6cDjUbwgZa5PuLK+MQ25zmNPl6uKhvli6Eb/xOB7ASnaZs\nAVjdTsYAI+Am+0B253ZhVJU=\n-----END PRIVATE KEY-----\n",
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

df = pd.DataFrame(rd, columns = ['id'])
dfl = df['id'].str.lower()

def cnt():
    cnt = int(len(set(df['id'])))
    return cnt
cnt()

st.write(f"Mamy **{cnt()}** samochodzików")

ti = st.text_input(label='szukaj')
til = ti.lower()

if til is not None :
    if til in dfl.values: 
        st.write("Mamy go") 
    else: 
        st.write("Kupujemy!")

dodaj_hw = st.button("Dodaj")
if dodaj_hw:
    sh.sheet1.update_cell(cnt()+2,1, ti)

refresh = st.button("Odswiez")
if refresh:
    cnt()

st.write(df)
