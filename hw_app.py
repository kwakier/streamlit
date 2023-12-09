import streamlit as st

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.experimental_connection("gsheets")

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)
