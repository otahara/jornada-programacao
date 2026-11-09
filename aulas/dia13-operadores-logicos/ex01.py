USUARIO_CERTO = "ana"
SENHA_CERTA = "Python123"

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == USUARIO_CERTO and senha == SENHA_CERTA:
    print("Acesso liberado")
else:
    print("Usuário ou senha incorretos")