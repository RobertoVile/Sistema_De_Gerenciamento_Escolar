import conexao
import media_final

def criar_tabela():
    conexao.conectar_banco()
    media_final.obter_medias_finais()
    
    criar_tabela_sql = """
    CREATE TABLE IF NOT EXISTS aluno (
        matricula INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data INTEGER,
        mes INTEGER,
        ano INTEGER,
        cpf INTEGER,
        telefone INTEGER,
        email TEXT,
        endereco TEXT,
        nomeResponsavel TEXT,
        nomeResponsavel2 TEXT,
        presenca INTEGER,
        falta INTEGER,
        serie INTEGER,
        turno TEXT,
        portugues_primeira_unidade REAL,
        matematica_primeira_unidade REAL,
        biologia_primeira_unidade REAL,
        fisica_primeira_unidade REAL,
        ingles_primeira_unidade REAL,
        filosofia_primeira_unidade REAL,
        artes_primeira_unidade REAL,
        quimica_primeira_unidade REAL,
        historia_primeira_unidade REAL,
        sociologia_primeira_unidade REAL,
        portugues_segunda_unidade REAL,
        matematica_segunda_unidade REAL,
        biologia_segunda_unidade REAL,
        fisica_segunda_unidade REAL,
        ingles_segunda_unidade REAL,
        filosofia_segunda_unidade REAL,
        artes_segunda_unidade REAL,
        quimica_segunda_unidade REAL,
        historia_segunda_unidade REAL,
        sociologia_segunda_unidade REAL,
        portugues_terceira_unidade REAL,
        matematica_terceira_unidade REAL,
        biologia_terceira_unidade REAL,
        fisica_terceira_unidade REAL,
        ingles_terceira_unidade REAL,
        filosofia_terceira_unidade REAL,
        artes_terceira_unidade REAL,
        quimica_terceira_unidade REAL,
        historia_terceira_unidade REAL,
        sociologia_terceira_unidade REAL,
        portugues_media_final REAL DEFAULT 0,
        matematica_media_final REAL DEFAULT 0,
        biologia_media_final REAL DEFAULT 0,
        fisica_media_final REAL DEFAULT 0,
        ingles_media_final REAL DEFAULT 0,
        filosofia_media_final REAL DEFAULT 0,
        artes_media_final REAL DEFAULT 0,
        quimica_media_final REAL DEFAULT 0,
        historia_media_final REAL DEFAULT 0,
        sociologia_media_final REAL DEFAULT 0,
        relatorio1 TEXT,
        relatorio2 TEXT,
        relatorio3 TEXT,
        relatorio4 TEXT,
        relatorio5 TEXT,
        relatorio6 TEXT,
        relatorioA1 TEXT,
        relatorioA2 TEXT,
        relatorioA3 TEXT
    )
    """
    
    conexao.cursor.execute(criar_tabela_sql)
    conexao.conn.commit()
