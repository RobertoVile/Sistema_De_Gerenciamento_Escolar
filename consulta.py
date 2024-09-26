import sqlite3
import conexao
import tabela
import media_final
def consultar_boletim():
    tabela.criar_tabela()
    #Chamando a função do cálculo das médias para ir atualizando
    media_final.obter_medias_finais()
    # Matricula
    matricula = input("Informe o número da matrícula que deseja consultar: ")
    try:
        # Pegando a matrícula da tabela
        resultado = conexao.conn.execute('''SELECT * FROM aluno WHERE matricula = ?''', (matricula,)).fetchall()
        if not resultado:
            print("Matrícula não encontrada!")
        else:
            for result in resultado:
                print(">>>>>>>>>><<<<<<<<<<\n")
                print(f"Matrícula: {result[0]}")
                print(f"Nome: {result[1]}")
                print(f"Presença: {result[11]}")
                print(f"Falta: {result[12]}")
                print(f"Série: {result[13]}")
                print(f"Turno: {result[14]}\n")
                print("Notas:")
                print(f"              (1ªUnidade ),    (2ªUnidade ),    (3ªUnidade )")
                print(f"  Português:     {result[15]}              {result[25]}              {result[35]}")
                print(f"  Matemática:    {result[16]}              {result[26]}              {result[36]}")
                print(f"  Biologia:      {result[17]}              {result[27]}              {result[37]}")
                print(f"  Física:        {result[18]}              {result[28]}              {result[38]}")
                print(f"  Inglês:        {result[19]}              {result[29]}              {result[39]}")
                print(f"  Filosofia:     {result[20]}              {result[30]}              {result[40]}")
                print(f"  Artes:         {result[21]}              {result[31]}              {result[41]}")
                print(f"  Química:       {result[22]}              {result[32]}              {result[42]}")
                print(f"  História:      {result[23]}              {result[33]}              {result[43]}")
                print(f"  Sociologia:    {result[24]}              {result[34]}              {result[44]}")
            
                print("\nMédias Finais:")
                print(f"  Português:  {result[45]}")
                print(f"  Matemática: {result[46]}")
                print(f"  Biologia:   {result[47]}")
                print(f"  Física:     {result[48]}")
                print(f"  Inglês:     {result[49]}")
                print(f"  Filosofia:  {result[50]}")
                print(f"  Artes:      {result[51]}")
                print(f"  Química:    {result[52]}")
                print(f"  História:   {result[53]}")
                print(f"  Sociologia: {result[54]}")
                
    except sqlite3.Error as erro:
        print("Erro ao encontrar aluno", erro)
    finally:
        conexao.conn.close()