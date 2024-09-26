import datetime


def nascimento():
    global data,mes,ano
    try:
        data = int(input("Informe o dia de nascimento do aluno (DD): "))
        mes = int(input("Informe o mês de nascimento do aluno (MM): "))
        ano = int(input("Informe o ano de nascimento do aluno (YYYY): "))
        datetime.datetime(ano, mes, data)
        return data,mes,ano
    
    except ValueError:
        print("Erro: Data de nascimento inválida. Verifique se os valores são válidos.")
        nascimento()
