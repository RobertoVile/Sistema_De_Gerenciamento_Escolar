import menu_aluno
import menu_pais
import menu_professor
import menu_diretor
import menu_principal
import verificar_senha
#oi
def main():
    while True:
        opcao = menu_principal.menu()
        
        if opcao == '1':
            menu_aluno.aluno()
            
        elif opcao == '2':
            menu_pais.pais()  
            
        elif opcao == '3':
            menu_professor.professor()
            
        elif opcao == '4':
            if verificar_senha.verificacao():
                menu_diretor.diretor()
            else:
                continue  # Volta ao menu principal se a senha estiver incorreta
            
        elif opcao == '5':
            print("Encerrando o programa...")
            break
            
        else:
            print("Opção inválida. Tente novamente.")

main()
