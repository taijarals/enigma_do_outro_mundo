import streamlit as st

st.set_page_config(page_title="App")

# inicializa sessão
if "usuario" not in st.session_state:
    st.session_state["usuario"] = None

st.title("🎮 Sistema")

st.write("Use o menu lateral para navegar.")