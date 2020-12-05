"""
Cassiano de Souza Santos
Trabalho 3 LP
"""


class MinhaData:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Criar um construtor que receba uma string e inicialize a data
    def __init__(self, string):
        lista = string.split("/")
        self.dia = int(lista[0])
        self.mes = int(lista[1])
        self.ano = int(lista[2])

    # Não entendi muito bem o que pediu
    def ToString(self):
        lista = []
        lista.append(self.dia)
        lista.append(self.mes)
        lista.append(self.ano)
        string = ''.join(lista)
        return string

    def compara(self, data):
        if (self.dia == data.dia) and (self.mes == data.mes) and (self.ano == data.ano):
            return 0

        if (self.ano == data.ano) and (self.mes == data.mes):
            if (self.dia > data.dia):
                return 1
            else:
                return -1
        if (self.ano == data.ano):
            if (self.mes > data.mes):
                return 1
            else:
                return -1
        if (self.ano > data.ano):
            return 1
        else:
            return -1


class DataComemorativa:
    nome = ""
    feriado = False
    Fmundial = False
    day = ""

    def __init__(self, nome, feriado, Fmundial, day):
        self.nome = nome
        self.feriado = feriado
        self.Fmundial = Fmundial
        self.day = day
        # print(f"{self.nome}, {self.feriado}, {self.Fmundial}, {self.day}")


class DatasComemorativas:
    def __init__(self):
        self.datas = []

    def adiciona_data(self, data):
        self.datas.append(data)

    def lista_datas(self):
        for data in self.datas:
            print(data.nome, data.feriado, data.Fmundial, data.day)

    def remove_data(self, nome):
        for data in self.datas:
            if nome in data.nome:
                del data.nome
                del data.day
                del data.feriado
                del data.Fmundial

    def horas_nao_trabalhadas(self):
        cont = 0
        for data in self.datas:
            if (data.feriado == True):
                cont+=1
        print(f"{cont*8}h")
        return cont*8

atual = MinhaData("05/12/2020")
natal = MinhaData("25/12/2020")
print(atual.compara(natal))
natal = DataComemorativa("Natal", True, True, "25/12/2020")
feriado = DatasComemorativas()
feriado.adiciona_data(natal)
feriado.horas_nao_trabalhadas()

