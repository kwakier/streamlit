import streamlit as st

##dodaj = st.Page("1_dodaj_wpis.py", title="Dodaj wpis", icon=":material/add_circle:")
##dashboard = st.Page("2_dashboard.py", title="Dashboard", icon=":material/insert_chart_outlined:")
hwapp = st.Page("3_hw_app.py", title="Hot Wheels", icon=":material/directions_car:")
hwdashboard = st.Page("4_hw_dashboard.py", title="HW Dashboard", icon=":material/directions_car:")

pg = st.navigation([hwapp, hwdashboard])
st.set_page_config(page_title="Moje appki", page_icon=":material/edit:")
pg.run()
