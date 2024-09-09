import streamlit as st

dodaj = st.Page("1_dodaj_wpis.py", title="Dodaj wpis", icon=":material/add_circle:")
dashboard = st.Page("2_dashboard.py", title="Dashboard", icon=":material/delete:")
hwapp = st.Page("3_hw_app.py", title="Hot Wheels", icon=":material/delete:")

pg = st.navigation([dodaj, dashboard, hwapp])
st.set_page_config(page_title="Moje appki", page_icon=":material/edit:")
pg.run()
