"""
Cassiano de Souza Santos
Trabalho 4 - LP
"""


class MinhaData:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    # Criar um construtor que receba uma string e inicialize a data
    def __init__(self, string):
        lista = string.split("/")
        self.__dia = int(lista[0])
        self.__mes = int(lista[1])
        self.__ano = int(lista[2])

    # Não entendi muito bem o que pediu
    def ToString(self):
        lista = []
        lista.append(self.__dia)
        lista.append(self.__mes)
        lista.append(self.__ano)
        string = ''.join(lista)
        return string

    def compara(self, data):
        if (self.__dia == data.dia) and (self.__mes == data.mes) and (self.__ano == data.ano):
            return 0

        if (self.__ano == data.ano) and (self.__mes == data.mes):
            if (self.__dia > data.__dia):
                return 1
            else:
                return -1
        if (self.__ano == data.ano):
            if (self.__mes > data.mes):
                return 1
            else:
                return -1
        if (self.__ano > data.ano):
            return 1
        else:
            return -1


class DataComemorativa:
    nome = ""
    feriado = False
    Fmundial = False
    day = ""

    def __init__(self, nome, feriado, Fmundial, day):
        self.__nome = nome
        self.__feriado = feriado
        self.__Fmundial = Fmundial
        self.__day = day

    @property
    def nome(self):
        return self.__nome

    @property
    def feriado(self):
        return self.__feriado

    @property
    def Fmundial(self):
        return self.__Fmundial

    @property
    def day(self):
        return self.__day


class DatasComemorativas:
    def __init__(self):
        self.__datas = []

    @property
    def datas(self):
        return self.__datas

    def adiciona_data(self, nome, feriado, Fmundial, day):
        self.__datas.append(DataComemorativa(nome, feriado, Fmundial, day))

    def lista_datas(self):
        for data in self.__datas:
            print(data.__nome, data.__feriado, data.__Fmundial, data.__day)

    def remove_data(self, nome):
        for data in self.__datas:
            if nome in data.__nome:
                del data.__nome
                del data.__day
                del data.__feriado
                del data.__Fmundial

    def horas_nao_trabalhadas(self):
        cont = 0
        for data in self.__datas:
            if (data.feriado == True):
                cont += 1
        print(f"{cont * 8}h")
        return cont * 8


atual = MinhaData("05/12/2020")
natal = MinhaData("25/12/2020")
print(atual.compara(natal))

natal = DatasComemorativas()
natal.adiciona_data("Natal", True, True, "25/12/2020")
natal.horas_nao_trabalhadas()

"""
>>>>>  Saída = -1
>>>>>  Saída = 8h
"""
