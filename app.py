import streamlit as st
from pages.login import render_login
from pages.home import render_home

st.set_page_config(page_title="App")

# inicializa sessão
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

# roteamento simples
if st.session_state["usuario"] is None:
    render_login()
else:
    render_home()