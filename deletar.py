import sqlite3
import logging
import tabela
import conexao

# Função para excluir um aluno
logging.basicConfig(level=logging.WARNING)

def excluir_aluno():
    tabela.criar_tabela()
    
    # Digitar a matricula do aluno
    matricula = input("Informe a matricula do aluno que deseja excluir do sistema: ")

    # Solicitar confirmação
    confirmacao = input(f'Você tem certeza que deseja excluir o aluno com matricula {matricula}? (s/n): ')
    
    if confirmacao == 's' or confirmacao == 'sim':
        try:
            conexao.cursor.execute('SELECT * FROM aluno WHERE matricula = ?', (matricula,))
            aluno = conexao.cursor.fetchone()
            
            if aluno:
                conexao.cursor.execute('DELETE FROM aluno WHERE matricula = ?', (matricula,))
                conexao.conn.commit()
                # logging.info(f'Aluno com matricula {matricula} foi excluído por {usuario.nome}.')
                print(f'Aluno com matrícula {matricula} foi excluído!')
            else:
                logging.warning(f'Aluno com matricula {matricula} não encontrado.')
                print("Aluno não encontrado.")
                 
        except sqlite3.Error as erro:
            print("Erro ao excluir aluno:", erro)
        
        finally:
            conexao.conn.close()
    else:
        print("Exclusão cancelada!")
        excluir_aluno()
   