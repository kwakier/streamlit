import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read( 
    worksheet="Arkusz1",
    ttl="10m",
    usecols=[0, 1],
    nrows=8,)

# Print results.
for row in df.itertuples():
    st.write(f"{row.id} introduced in a :{row.year}:")
