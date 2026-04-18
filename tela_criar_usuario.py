import streamlit as st
from db.conexao import supabase

st.set_page_config(page_title="Cadastro de Usuário")

st.title("📝 Cadastro de Usuário")

with st.form("cadastro_usuario"):
    nick = st.text_input("Nick")
    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")
    tipo = st.selectbox("Tipo de Usuário", ["user", "admin", "moderador"])
    
    submit = st.form_submit_button("Cadastrar")

if submit:
    # validações básicas
    if not nick or not email or not senha:
        st.warning("Preencha todos os campos obrigatórios!")
    
    else:
        try:
            response = supabase.table("usuario").insert({
                "nick_usuario": nick,
                "email_usuario": email,
                "senha_usuario": senha,
                "tipo_usuario": tipo
            }).execute()

            if response.data:
                st.success("Usuário cadastrado com sucesso! 🎉")
            else:
                st.error("Erro ao cadastrar usuário")

        except Exception as e:
            st.error(f"Erro: {e}")