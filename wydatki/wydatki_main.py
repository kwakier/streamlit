import streamlit as st

dodaj_wpis_wydatkow = st.Page("1_dodaj_wpis.py", title="Dodaj wpis", icon=":material/add_circle:")
dashboard = st.Page("2_dashboard.py", title="Dashboard", icon=":material/delete:")
hw_app = st.Page("3_hw_app.py", title="Hot Wheels", icon=":material/delete:")

pg = st.navigation([dodaj_wpis_wydatkow, dashboard, hw_app])
st.set_page_config(page_title="Moje appki", page_icon=":material/edit:")
pg.run()
