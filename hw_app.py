import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection
#st.cache(persist=True, allow_output_mutation=True)

#st.file_uploader(type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False)

# Create a connection object.
url = "https://docs.google.com/spreadsheets/d/1yi769GiV0MsO2hHCJHhQJaIL96_3wu955LZxo79hOkU/edit?pli=1#gid=0"

conn = st.connection("gsheets", type=GSheetsConnection)

rd = conn.read( 
    spreadsheet=url,      
    worksheet="Arkusz1",
    ttl="10m",
    usecols=[0]
    )
st.image(hwlogo.png)
cnt = rd.count()
st.write(cnt)

#Print results (simple).
#for row in rd.itertuples():
#    st.write(f"{row.id}")

#Print results (pretty).
df = pd.DataFrame(rd, columns = ['id'])
dfl = df['id'].str.lower()


#st.write(dfl)
st.write(df)

ti = st.text_input(label='szukaj')
til = ti.lower()

if til is not None :
    if til in dfl.values: 
        st.write("Mamy go") 
    else: 
        st.write("Kupujemy!")
