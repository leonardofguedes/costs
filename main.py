class Pessoa:

    expense = {}  #dict com despesas e o dia respectivo
    tot = 0  # valor total de despesas

    def __init__(self, nome, salary, years_of_work):
        self.__nome = nome
        self.__salary = salary
        self.__years_of_work = years_of_work
        self.__totals = salary * 12 * years_of_work

    @classmethod
    def expenses(cls, day_week, exp):  #adicionar despesa e dia específico
        Pessoa.expense[day_week] = exp
        Pessoa.tot += exp


    def profit(self):  # subtrai do saláriototal as despesas semanais multipl. por 4 e depois pelos anos de trabalho
        return f'Total profit in {self.__years_of_work} years: {self.__totals - Pessoa.tot*4*12*self.__years_of_work}'\
               f' Total Expenses: {Pessoa.tot*4*12*self.__years_of_work} Total Earnings: {self.__totals}'\
                f' Despesa semanal: {Pessoa.tot}'
