from db.conexao import supabase

# ------------------------
# LOGIN (Auth Supabase)
# ------------------------
def login_usuario(email, senha):
    try:
        response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": senha
        })

        return response.user

    except Exception:
        return None


# ------------------------
# CADASTRO (Auth + Perfil)
# ------------------------
def cadastrar_usuario(nick, email, senha, tipo):
    try:
        # cria no Auth
        auth_response = supabase.auth.sign_up({
            "email": email,
            "password": senha
        })

        user = auth_response.user

        if user is None:
            return None

        # cria perfil
        supabase.table("usuario").insert({
            "id": user.id,
            "nick_usuario": nick,
            "email_usuario": email,
            "tipo_usuario": tipo,
            "pontuacao_usuario": 0,
            "nivel_usuario": 1
        }).execute()

        return user

    except Exception as e:
        print(e)
        return None


# ------------------------
# BUSCAR PERFIL
# ------------------------
def buscar_perfil(user_id):
    response = supabase.table("usuario") \
        .select("*") \
        .eq("id", user_id) \
        .execute()

    if response.data:
        return response.data[0]

    return None


# ------------------------
# LOGOUT
# ------------------------
def logout_usuario():
    supabase.auth.sign_out()
    return None