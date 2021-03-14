"""
Cassiano de Souza Santos
Trabalho 4 - LP
"""


class MinhaData:

    # Criar um construtor que receba o dia, mês e ano desta data.
    def __init__(self, dia, mes, ano, nome):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.nome = nome

    # Criar um construtor que receba uma string e inicialize a data.
    def __init__(self, data, nome):
        self.nome = nome
        lista = data.split("/")
        self.dia = int(lista[0])
        self.mes = int(lista[1])
        self.ano = int(lista[2])

    def __str__(self):  # toString
        return f"{self.dia}/{self.mes}/{self.ano}"

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


class DataComemorativa(MinhaData):

    def __init__(self, nome, data, fMundial, fNormal):
        super().__init__(nome, data)
        self.fNormal = fNormal
        self.fMundial = fMundial


class DatasComemorativas:
    def __init__(self):
        self.feriados = []

    def adiciona(self, data):
        self.feriados.append(data)

    def remove(self, nome):
        for data in self.feriados:
            if data.nome.lower() == nome.lower():
                self.feriados.remove(data)

    def horas_nao_trabalhadas(self):
        return len(self.feriados)*8


atual = MinhaData("06/12/2020", "atual")
natal = MinhaData("25/12/2020", "natal")
print(atual.compara(natal))

feriados = DatasComemorativas()
feriados.adiciona(natal)
print(feriados.horas_nao_trabalhadas())

"""
SAÍDA = -1
SAÍDA = 8h
"""
