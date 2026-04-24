import streamlit as st
from db.conexao import supabase

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
            return

        try:
            # 🔐 1. Cria usuário no Auth
            auth_response = supabase.auth.sign_up({
                "email": email,
                "password": senha
            })

            user = auth_response.user

            if user is None:
                st.error("Erro ao criar usuário no Auth")
                return

            # 🗄️ 2. Salva dados na tabela usuario
            supabase.table("usuario").insert({
                "id": user.id,  # 🔥 chave de ligação com Auth
                "nick_usuario": nick,
                "email_usuario": email,
                "tipo_usuario": tipo
            }).execute()

            st.success("Usuário cadastrado com sucesso! 🎉")

        except Exception as e:
            st.error(f"Erro: {e}")