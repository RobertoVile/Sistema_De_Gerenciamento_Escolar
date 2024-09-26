import sqlite3
import conexao

def gerar_relatorio_anual():
    try:
        conexao.conectar_banco()
        matricula = int(input("Informe a matricula do aluno para gerar o relatório anual: "))
        
        # Obter o aluno
        conexao.cursor.execute("SELECT * FROM aluno WHERE matricula =?", (matricula,))
        aluno = conexao.cursor.fetchone()

        if aluno:
            relatorioA1 = input("Informe o relatório sobre o desempenho: ")
            relatorioA2 = input("Informe o relatório sobre a presença:  ")
            relatorioA3 = input("Informe o relatório sobre o comportamento:  ")
            
            conexao.cursor.execute("""
                UPDATE aluno
                SET relatorioA1 = ?, relatorioA2 = ?, relatorioA3 = ?
                WHERE matricula = ?
            """, (relatorioA1, relatorioA2, relatorioA3, matricula))

            
            conexao.conn.commit()
            print("Relatório anual atualizado com sucesso!")
        else:
            print("Aluno não encontrado!")

    except sqlite3.Error as erro:
        print("Erro ao gerar o relatório anual!", erro)
    finally:
        conexao.conn.commit()
        conexao.conn.close()
