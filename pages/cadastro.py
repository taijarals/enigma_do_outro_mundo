import streamlit as st
from services.auth import cadastrar_usuario

def render_cadastro():
    st.title("📝 Cadastro de Usuário")

    with st.form("cadastro_usuario"):
        nick = st.text_input("Nick")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        tipo = st.selectbox("Tipo de Usuário", ["user", "admin", "moderador"])

        submit = st.form_submit_button("Cadastrar")

    if submit:
        if not nick or not email or not senha:
            st.warning("Preencha todos os campos!")
        else:
            user = cadastrar_usuario(nick, email, senha, tipo)

            if user:
                st.success("Usuário cadastrado com sucesso! 🎉")
            else:
                st.error("Erro ao cadastrar usuário")

    st.markdown("---")

    if st.button("⬅️ Voltar para login"):
        st.session_state["tela"] = "login"
        st.rerun()