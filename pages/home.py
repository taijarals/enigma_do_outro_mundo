import streamlit as st
from services.auth import logout_usuario

def render_home():
    usuario = st.session_state["usuario"]

    st.title(f"👋 Bem-vindo, {usuario['nick_usuario']}")

    st.write("📧 Email:", usuario["email_usuario"])
    st.write("🏆 Pontuação:", usuario.get("pontuacao_usuario", 0))
    st.write("⭐ Nível:", usuario.get("nivel_usuario", 1))

    if st.button("Sair"):
        st.session_state["usuario"] = logout_usuario()
        st.session_state["tela"] = "login"
        st.rerun()