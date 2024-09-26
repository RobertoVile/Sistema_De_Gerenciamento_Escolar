def verificacao():
    senha_correta = "escolamoderna123"
    senha = input("Insira a senha de verificação: ")
    while senha != senha_correta:
        print("Senha incorreta. Voltando ao menu principal.")
        return False
    return True