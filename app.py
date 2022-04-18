from main import Pessoa


def earnings():         # -- >função para capturar as informações nome, salário e tempo de trabalho
    try:
        name = str(input('Informa seu nome:')).capitalize().strip()
        month_payment = int(input('Informe seu salário mensal líquido:'))
        years_job = int(input('Informe a quantidade de anos de trabalho:'))
        user = Pessoa(name, month_payment, years_job)
        return user         # -- > retornará o user que será usado na função expenses abaixo

    except:
        print('Você deve escolher um número inteiro.')


def expenses(user):  # -- > função para adicionar as despesas
    while True:
        add_expense = str(input('Deseja adicionar despesas? [S] ou [N]')).strip().upper()
        if add_expense == 'S':
            print('Informe o dia da semana e a qual é sua média de despesas')
            dow = input('Dia da semana: ->')
            desp = int(input('Despesa: ->'))
            user.expenses(dow, desp)  # -- > a função usada aqui é a de main.py
        elif add_expense == 'N':
            return show(user)  # -- > qndo n adicionar mais despesas, ele retorna o user para ser utilizado em show
        else:
            print('Wrong answer')


def show(user):
    print(user.profit())


def app():
    while True:
        expenses(earnings())


if __name__ == '__main__':
    app()