import sqlite3
import conexao

def imprimir_relatorio_anual():
    try:
        # Conectar banco
        conexao.conectar_banco()

        matricula = int(input("Informe a matrícula do aluno para imprimir os relatórios: "))

        # Obter o relatório sobre o desempenho
        conexao.cursor.execute("SELECT relatorioA1 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA1 = conexao.cursor.fetchone()

        # Obter o relatório sobre a presença
        conexao.cursor.execute("SELECT relatorioA2 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA2 = conexao.cursor.fetchone()

        # Obter o relatório sobre o comportamento
        conexao.cursor.execute("SELECT relatorioA3 FROM aluno WHERE matricula=?", (matricula,))
        relatorioA3 = conexao.cursor.fetchone()

        # Exibir os relatórios
        print("\nRelatório sobre o desempenho:")
        if relatorioA1 and relatorioA1[0]:
            print(relatorioA1[0])
        else:
            print("Nenhum relatório disponível.")

        print("\nRelatório sobre a presença:")
        if relatorioA2 and relatorioA2[0]:
            print(relatorioA2[0])
        else:
            print("Nenhum relatório disponível.")

        print("\nRelatório sobre o comportamento:")
        if relatorioA3 and relatorioA3[0]:
            print(relatorioA3[0])
        else:
            print("Nenhum relatório disponível.")

    except sqlite3.Error as erro:
        print("Erro ao imprimir os relatórios!", erro)
    finally:
        conexao.conn.close()

