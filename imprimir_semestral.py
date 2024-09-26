import sqlite3
import conexao


def imprimir_relatorio_semestral():
    try:
        conexao.conectar_banco()
        matricula = input("Informe a matrícula do aluno para imprimir os relatórios: ")
        semstral = input("Imprimir o 1º ou 2º semestre? ")
            # Imprimir o 1º relatório sobre o desempenho
        if semstral == '1':
            conexao.cursor.execute(
            "SELECT relatorio1 FROM aluno WHERE matricula=?", (matricula,))
            relatorio1= conexao.cursor.fetchone()

            # Imprimr o 1º relatório sobre a presença
            conexao.cursor.execute(
                "SELECT relatorio2 FROM aluno WHERE matricula=?", (matricula,))
            relatorio2 = conexao.cursor.fetchone()

            # Imprimir o 1º relatório sobre o comportamento
            conexao.cursor.execute(
                "SELECT relatorio3 FROM aluno WHERE matricula=?", (matricula,))
            relatorio3 = conexao.cursor.fetchone()

            print("\nRelatório sobre o desempenho:")
            print(relatorio1[0]
                  if relatorio1 else "Nenhum relatório disponível.")

            print("\nRelatório sobre a presença:")
            print(relatorio2[0]
                  if relatorio2 else "Nenhum relatório disponível.")

            print("\nRelatório sobre o comportamento:")
            print(relatorio3[0]
                  if relatorio3 else "Nenhum relatório disponível.")

        #Imprimir o 2º relatório sobre o desempenho
        elif semstral == '2':
            conexao.cursor.execute(
            "SELECT relatorio4 FROM aluno WHERE matricula=?", (matricula,))
            relatorio4 = conexao.cursor.fetchone()

            #Imprimir o 2º relatório sobre a presença
            conexao.cursor.execute(
                "SELECT relatorio5 FROM aluno WHERE matricula=?", (matricula,))
            relatorio5 = conexao.cursor.fetchone()

            #Imprimir o 2º relatório sobre o comportamento
            conexao.cursor.execute(
                "SELECT relatorio6 FROM aluno WHERE matricula=?", (matricula,))
            relatorio6 = conexao.cursor.fetchone()

            print("\nRelatório sobre o desempenho:")
            print(relatorio4[0]
                  if relatorio4 else "Nenhum relatório disponível.")

            print("\nRelatório sobre a presença:")
            print(relatorio5[0]
                  if relatorio5 else "Nenhum relatório disponível.")

            print("\nRelatório sobre o comportamento:")
            print(relatorio6[0]
                  if relatorio6 else "Nenhum relatório disponível.")
            
    except sqlite3.Error as erro:
            print("Erro ao imprimir os relatórios!", erro)
    finally:
            conexao.conn.close()
