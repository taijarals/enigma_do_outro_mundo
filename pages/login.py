import streamlit as st
from services.auth import login_usuario

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
                st.session_state["usuario"] = user
                st.success("Login realizado!")
                st.rerun()
            else:
                st.error("Email ou senha inválidos")

def login_usuario(email, senha):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": senha
        })

        return response.user

    except Exception:
        return None