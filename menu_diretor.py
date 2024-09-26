import cadastrar_aluno
import deletar
import gerar_semestral
import gerar_anual

def diretor():
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
    
    print(f"{GREEN}1. Adicionar Aluno{RESET}")
    print(f"{GREEN}2. Deletar um aluno {RESET}")
    print(f"{GREEN}3. Gerar relatorio semestral {RESET}")
    print(f"{GREEN}4. Gerar relatorio anual {RESET}")
    print(f"{GREEN}(Qualquer outro valor para sair). Sair{RESET}")

    global opcao
    opcao = input(f"{BLUE} Digite a opção escolhida {RESET}")

    if opcao == '1':
        cadastrar_aluno.cadastro()
    elif opcao == '2':
        deletar.excluir_aluno()
    elif opcao == '3':
        gerar_semestral.gerar_relatorio_semestral()
    elif opcao == '4':
        gerar_anual.gerar_relatorio_anual()