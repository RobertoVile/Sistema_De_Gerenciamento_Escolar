def menu():
    #Código de cores para o menu
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    #Menu para escolher tipo de usuário da Escola
    print(BOLD + BLUE + "="*50 + RESET)
    print(BOLD + GREEN + "                 ESCOLA MODERNA" + RESET)
    print(BOLD + BLUE + "="*50 + RESET)
    print()
    #incluir função em que direcione pra ou menu de aluno, responsavel, professor ou diretoria.
    print(f"{GREEN}1. Aluno{RESET}")
    print(f"{GREEN}2. Responsável{RESET}")
    print(f"{GREEN}3. Professor{RESET}")
    print(f"{GREEN}4. Diretoria{RESET}")
    print(f"{GREEN}5. Sair{RESET}")
    global opcao      
    opcao = input (f"{BLUE}Digite a opção escolhida: {RESET}")
    return opcao
    

   
