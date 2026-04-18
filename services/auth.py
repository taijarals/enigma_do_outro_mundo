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