import sqlite3
import conexao
import verificar_login


def notas():
    global nota
    resultado = '1'
    while resultado == '1':
        # Verifica as credenciais do professor e obtém a matéria
        verificar_login.verificar_credenciais()

        # Consulta a matéria do professor
        resultado = conexao.conn.execute('''
            SELECT materia FROM professor WHERE email = ? AND senha = ?
        ''', (verificar_login.email, verificar_login.senha)).fetchone()

        if not resultado:
            print("Professor não encontrado!")
            break

        matricula = input("Informe a matrícula que deseja consultar: ")
        try:
                # Consultar aluno pelo número de matrícula
                resultado_aluno = conexao.conn.execute('''
                    SELECT * FROM aluno WHERE matricula = ?
                ''', (matricula,)).fetchone()

                if not resultado_aluno:
                    print("Matrícula não encontrada!")
                    break

                # Pede a unidade para alterar as notas
                option = int(input("Qual unidade deseja alterar a nota? (1° a 3°) "))

                if option < 1 or option > 3:
                    print("Opção inválida!")
                    notas()

                # Pede a nota apenas para a matéria específica
                if resultado[0] == "portugues":
                    nota = float(input("Informe a Nota de Português: "))
                elif resultado[0] == "matematica":
                    nota = float(input("Informe a Nota de Matemática: "))
                elif resultado[0] == "biologia":
                    nota = float(input("Informe a Nota de Biologia: "))
                elif resultado[0] == "fisica":
                    nota = float(input("Informe a Nota de Física: "))
                elif resultado[0] == "ingles":
                    nota = float(input("Informe a Nota de Inglês: "))
                elif resultado[0] == "filosofia":
                    nota = float(input("Informe a Nota de Filosofia: "))
                elif resultado[0] == "artes":
                    nota = float(input("Informe a Nota de Artes: "))
                elif resultado[0] == "quimica":
                    nota = float(input("Informe a Nota de Química: "))
                elif resultado[0] == "historia":
                    nota = float(input("Informe a Nota de História: "))
                elif resultado[0] == "sociologia":
                    nota = float(input("Informe a Nota de Sociologia: "))
                elif resultado[0] == "projeto_vida":
                    nota = float(input("Informe a Nota de Projeto de Vida: "))

                else:
                    print("Matéria não reconhecida!")
                    return

                # Atualiza as notas com base na opção escolhida usando o valor da variável resultado (no caso, a matéria)
                if option == 1:
                    atualizar_notas = f'''
                        UPDATE aluno
                        SET {resultado[0]}_primeira_unidade = ?
                        WHERE matricula = ?
                    '''
                elif option == 2:
                    atualizar_notas = f'''
                        UPDATE aluno
                        SET {resultado[0]}_segunda_unidade = ?
                        WHERE matricula = ?
                    '''
                elif option == 3:
                    atualizar_notas = f'''
                        UPDATE aluno
                        SET {resultado[0]}_terceira_unidade = ?
                        WHERE matricula = ?
                    '''

                conexao.conn.execute(atualizar_notas, (nota, matricula))
                conexao.conn.commit()
                print("Nota atualizada com sucesso!")
                resultado = input("Deseja continuar alterando as notas? ('1' para sim e '0' para não) ")

                if resultado != '1':
                    break
                

        except sqlite3.Error as erro:
            print("Erro ao atualizar notas!", erro)

        finally:
            conexao.conn.close()
