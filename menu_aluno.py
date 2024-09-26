
import consulta
def aluno():          
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    #Menu para escolher tipo de usuário da Escolha

    print(BOLD + BLUE + "="*50 + RESET)
    print(BOLD + GREEN + "                 ESCOLA MODERNA" + RESET)
    print(BOLD + BLUE + "="*50 + RESET)
    print()
    print(f"{GREEN}1. Consultar Boletim Escolar{RESET}")
    print(f"{GREEN}2. Sair {RESET}")
    global opcao    
    opcao = input (f"{BLUE} Digite a opção escolhida {RESET}")

    if opcao == '1':
         #Função para ler o boletim
         consulta.consultar_boletim()
    else:
        print(f"{BLUE} Digite um valor válido...{RESET}")
    