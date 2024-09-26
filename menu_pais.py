import consulta
import imprimir_semestral
import imprimir_anual

def pais():
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"

    # Menu para escolher tipo de usuário da Escola
    print(BOLD + BLUE + "="*50 + RESET)
    print(BOLD + GREEN + "                 ESCOLA MODERNA" + RESET)
    print(BOLD + BLUE + "="*50 + RESET)
    print()
    print(f"{GREEN}1. Consultar Boletim Escolar {RESET}")
    print(f"{GREEN}2. Acessar relatorio semestral{RESET}")
    print(f"{GREEN}3. Acessar relatorio anual{RESET}")
    print(f"{GREEN}(Qualquer outro valor). Sair{RESET}")

    global opcao      
    opcao = input(f"{BLUE} Digite a opção escolhida {RESET}")

    if opcao == '1':
        consulta.consultar_boletim() 
    elif opcao == '2':
        imprimir_semestral.imprimir_relatorio_semestral()
    elif opcao == '3':
        imprimir_anual.imprimir_relatorio_anual()
    else:
        print(f"{BLUE} Valor inválido... {RESET}")