import streamlit as st
from services.auth import login_usuario, buscar_perfil

def render_login():
    st.title("🔐 Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        submit = st.form_submit_button("Entrar")

    if submit:
        if not email or not senha:
            st.warning("Preencha todos os campos")
        else:
            user = login_usuario(email, senha)

            if user:
                perfil = buscar_perfil(user.id)
                st.session_state["usuario"] = perfil
                st.success("Login realizado!")
                st.rerun()
            else:
                st.error("Email ou senha inválidos")

    st.markdown("---")

    if st.button("👉 Criar usuário"):
        st.switch_page("pages/cadastro.py")


# 🔥 ESSENCIAL
render_login()