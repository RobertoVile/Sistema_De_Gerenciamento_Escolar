import sqlite3
import conexao
import tabela

      
def continuar():
    
    escolha = input("Deseja realmente sair? S/Sim para sair/Qualquer outro valor para Continuar: ").lower()
    if escolha == 's' or escolha == 'sim':
        opcao = '3'
    else:
        presenca()   

def presenca():
    try:
        opcao = 0
        while opcao == 0:
            # Conectar ao banco de dados e a tabela
            
            tabela.criar_tabela()
            
            # Pede matrícula do aluno
            matricula = input("Informe a matrícula que deseja atualizar a presença: ")
            resultado = conexao.conn.execute('''SELECT * FROM aluno WHERE matricula = ? ''', (matricula,)).fetchall()
            
            if resultado == []:
                print("Matrícula não encontrada!")
                break
            else:
                for result in resultado:
                    opcao = input("O Aluno esteve na aula? \n1. Presença\n2. Falta\n \nEscolha uma opção: ")

                    if opcao == '1':
                        # Comando SQL para atualizar a presença
                        print("Presenca inserida!")
                        att = '''UPDATE aluno SET presenca = presenca + 1 WHERE matricula = ? '''
                        conexao.cursor.execute(att, (matricula,))
                        conexao.conn.commit()

                    elif opcao == '2':
                        print("Falta inserida!")
                        att = '''UPDATE aluno SET falta = falta + 1 WHERE matricula = ? '''
                        conexao.cursor.execute(att, (matricula,))
                        conexao.conn.commit()
                    else:
                        continuar()

          
    except sqlite3.Error as erro:
        print("Erro ao atualizar presença:", erro)
    
    finally:
        conexao.conn.commit()
        conexao.conn.close()