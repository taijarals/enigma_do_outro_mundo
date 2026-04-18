import streamlit as st
from services.auth import logout_usuario

def render_home():
    usuario = st.session_state["usuario"]

    st.title(f"👋 Bem-vindo, {usuario['nick_usuario']}")

    st.write("📧 Email:", usuario["email_usuario"])
    st.write("🏆 Pontuação:", usuario["pontuacao_usuario"])
    st.write("⭐ Nível:", usuario["nivel_usuario"])

    if st.button("Sair"):
        st.session_state["usuario"] = logout_usuario()
        st.rerun()