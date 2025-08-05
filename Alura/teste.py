# login.py

def authenticate(user_input, password_input):
    # Vulnerabilidade: senha hardcoded
    stored_username = "admin"
    stored_password = "P@ssw0rd123"  # <- hardcoded credential (CWE-798)

    if user_input == stored_username and password_input == stored_password:
        print("Acesso concedido.")
    else:
        print("Usuário ou senha incorretos.")

if __name__ == "__main__":
    user = input("Usuário: ")
    pwd = input("Senha: ")
    authenticate(user, pwd)
