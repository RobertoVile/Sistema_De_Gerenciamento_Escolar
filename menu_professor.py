import atualizar_notas
import frequencia

def professor():
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    #Menu para escolher opção
    print(BOLD + BLUE + "="*50 + RESET)
    print(BOLD + GREEN + "                 ESCOLA MODERNA" + RESET)
    print(BOLD + BLUE + "="*50 + RESET)
    print()
    print(f"{GREEN}1. Atualizar  Notas{RESET}")
    print(f"{GREEN}2. Registrar presença e falta{RESET}")
    print(f"{GREEN}(Qualquer outro valor). Para sair{RESET}")
    global opcao
    opcao = input (f"{BLUE} Digite a opção escolhida {RESET}")

    if opcao == '1':
        atualizar_notas.notas()
         
  
    elif opcao == '2':
   	  frequencia.presenca()
    
