import streamlit as st
from pages.login import render_login
from pages.cadastro import render_cadastro
from pages.home import render_home

st.set_page_config(page_title="App")

# estado inicial
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

if "tela" not in st.session_state:
    st.session_state["tela"] = "login"

# fluxo
if st.session_state["usuario"] is None:

    if st.session_state["tela"] == "login":
        render_login()

    elif st.session_state["tela"] == "cadastro":
        render_cadastro()

else:
    render_home()