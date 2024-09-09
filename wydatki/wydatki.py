import streamlit as st

dodaj_page = st.Page("2_dodaj.py", title="Dodaj wpis", icon=":material/add_circle:")
dash_page = st.Page("1_dashboard.py", title="Dashboard", icon=":material/space_dashboard:")

pg = st.navigation([dodaj_page, dash_page])
st.set_page_config(page_title="Wydatki", page_icon=":material/edit:")
pg.run()
