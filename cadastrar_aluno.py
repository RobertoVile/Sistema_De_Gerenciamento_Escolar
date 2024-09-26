import sqlite3
import conexao
import tabela
import verificar_data
import primeiraU
import segundaU
import terceiraU

def cadastro():
    try:
        # Conectar ao banco
        conexao.conectar_banco()
        tabela.criar_tabela()
        
        # Coletar dados do usuário
        nome = input("Informe o nome completo do aluno: ")
        verificar_data.nascimento()
        cpf = int(input("Informe o CPF do aluno: "))
        telefone = input("Informe seu N° de Telefone (Responsável): ")
        email = input("Informe seu email (Responsável): ")
        endereco = input("Informe seu Endereço: ")
        nomeResponsavel = input("Informe o nome do responsável: ")
        nomeResponsavel2 = input("Informe o nome do segundo responsável (deixe em branco se não houver): ") or None
        serie = int(input("Informe a série do aluno (1° a 3° ): "))
        if serie <= 0 or serie > 3:
            print("Série inválida. Tente novamente.")
            return
        turno = input("Informe o turno do aluno: ")
        if turno not in ["matutino", "vespertino", "noturno"]:
            print("Turno inválido. Tente novamente.")
            return
        
        # Definindo relatórios
        relatorio1 = None
        relatorio2 = None
        relatorio3 = None
        relatorio4 = None
        relatorio5 = None
        relatorio6 = None
        relatorioA1 = None
        relatorioA2 = None
        relatorioA3 = None
        
        # Coletando notas de unidades
        primeiraU.primeira_unidade()
        segundaU.segunda_unidade()
        terceiraU.terceira_unidade()

        presenca = 0
        falta = 0
        
        # Comando SQL para inserção
        inserir_aluno = """
        INSERT INTO aluno (
            nome, data, mes, ano, cpf, telefone, email, endereco, nomeResponsavel, nomeResponsavel2, 
            presenca, falta, serie, turno, 
            portugues_primeira_unidade, matematica_primeira_unidade, biologia_primeira_unidade,
            fisica_primeira_unidade, ingles_primeira_unidade, filosofia_primeira_unidade,
            artes_primeira_unidade, quimica_primeira_unidade, historia_primeira_unidade,
            sociologia_primeira_unidade, 
            portugues_segunda_unidade, matematica_segunda_unidade, biologia_segunda_unidade,
            fisica_segunda_unidade, ingles_segunda_unidade, filosofia_segunda_unidade,
            artes_segunda_unidade, quimica_segunda_unidade, historia_segunda_unidade,
            sociologia_segunda_unidade, 
            portugues_terceira_unidade, matematica_terceira_unidade, biologia_terceira_unidade,
            fisica_terceira_unidade, ingles_terceira_unidade, filosofia_terceira_unidade,
            artes_terceira_unidade, quimica_terceira_unidade, historia_terceira_unidade,
            sociologia_terceira_unidade, 
            relatorio1, relatorio2, relatorio3, relatorio4, relatorio5 ,relatorio6, relatorioA1, relatorioA2, relatorioA3
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)
        """

        # Valores a serem inseridos
        valores = (
            nome,
            verificar_data.data,
            verificar_data.mes,
            verificar_data.ano,
            cpf,
            telefone,
            email,
            endereco,
            nomeResponsavel,
            nomeResponsavel2,
            presenca,
            falta,
            serie,
            turno,
            primeiraU.portugues_primeira_unidade,
            primeiraU.matematica_primeira_unidade,
            primeiraU.biologia_primeira_unidade,
            primeiraU.fisica_primeira_unidade,
            primeiraU.ingles_primeira_unidade,
            primeiraU.filosofia_primeira_unidade,
            primeiraU.artes_primeira_unidade,
            primeiraU.quimica_primeira_unidade,
            primeiraU.historia_primeira_unidade,
            primeiraU.sociologia_primeira_unidade,
            segundaU.portugues_segunda_unidade,
            segundaU.matematica_segunda_unidade,
            segundaU.biologia_segunda_unidade,
            segundaU.fisica_segunda_unidade,
            segundaU.ingles_segunda_unidade,
            segundaU.filosofia_segunda_unidade,
            segundaU.artes_segunda_unidade,
            segundaU.quimica_segunda_unidade,
            segundaU.historia_segunda_unidade,
            segundaU.sociologia_segunda_unidade,
            terceiraU.portugues_terceira_unidade,
            terceiraU.matematica_terceira_unidade,
            terceiraU.biologia_terceira_unidade,
            terceiraU.fisica_terceira_unidade,
            terceiraU.ingles_terceira_unidade,
            terceiraU.filosofia_terceira_unidade,
            terceiraU.artes_terceira_unidade,
            terceiraU.quimica_terceira_unidade,
            terceiraU.historia_terceira_unidade,
            terceiraU.sociologia_terceira_unidade,
            relatorio1,
            relatorio2,
            relatorio3,
            relatorio4,
            relatorio5,
            relatorio6,
            relatorioA1,
            relatorioA2,
            relatorioA3
        )

        # Executa o insert e passa os valores 
        conexao.cursor.execute(inserir_aluno, valores)
        conexao.conn.commit()

        print("O aluno foi cadastrado com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao cadastrar aluno!", erro)

    finally:
        conexao.conn.close()
