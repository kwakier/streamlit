import streamlit as st

pg = st.navigation([st.Page("2_dodaj.py"), st.Page("1_dashboard.py")])
pg.run()

import streamlit as st

create_page = st.Page("2_dodaj.py", title="Dodaj wpis", icon=":material/add_circle:")
delete_page = st.Page("1_dashboard.py", title="Dashboard", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Wydatki", page_icon=":material/edit:")
pg.run()
