import sqlite3
import conexao

def gerar_relatorio_semestral():
    try:
        
        conexao.conectar_banco()
        matricula = int(input("Informe a matrícula do aluno para gerar o relatório: "))
        
        # Obter o aluno
        
        conexao.cursor.execute("SELECT * FROM aluno WHERE matricula=?", (matricula,))
        aluno = conexao.cursor.fetchone()
        opcaoSemestre = input("Qual semestre você deseja gerar o relatório (1 ou 2): ")

        if aluno:
            if opcaoSemestre == '1':
                relatorio1 = input("Informe o relatório sobre o desempenho: ")
                relatorio2 = input("Informe o relatório sobre a presença: ")
                relatorio3 = input("Informe o relatório sobre o comportamento: ")
                
                conexao.cursor.execute("""
                UPDATE aluno
                SET relatorio1 = ?, relatorio2 = ?, relatorio3 = ?
                WHERE matricula = ?
            """, (relatorio1, relatorio2, relatorio3, matricula))
                
            elif opcaoSemestre == '2':
                relatorio4 = input("Informe o relatório sobre o desempenho: ")
                relatorio5 = input("Informe o relatório sobre a presença: ")
                relatorio6 = input("Informe o relatório sobre o comportamento: ")
                
                conexao.cursor.execute("""
                UPDATE aluno
                SET relatorio4 = ?, relatorio5 = ?, relatorio6 = ?
                WHERE matricula = ?
            """, (relatorio4, relatorio5, relatorio6, matricula))
                
            conexao.conn.commit()
            print("Relatório atualizado com sucesso!")
        else:
            print("Aluno não encontrado!")

    except sqlite3.Error as erro:
        print("Erro ao gerar o relatório!", erro)
    finally:
        conexao.conn.close()
