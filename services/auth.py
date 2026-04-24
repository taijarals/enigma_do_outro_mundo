from db.conexao import supabase

def login_usuario(email, senha):
    response = supabase.table("usuario") \
        .select("*") \
        .eq("email_usuario", email) \
        .eq("senha_usuario", senha) \
        .execute()

    if response.data:
        return response.data[0]
    return None


def logout_usuario():
    return None

    from supabase import create_client

#funcao de cadastro de usuario
def cadastrar_usuario(email, senha):
    try:
        response = supabase.auth.sign_up({
            "email": email,
            "password": senha
        })
        return response.user
    except Exception as e:
        print(e)
        return None