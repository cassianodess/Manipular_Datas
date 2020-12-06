"""
Cassiano de Souza Santos
Trabalho 4 - LP
"""


class MinhaData:

    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Criar um construtor que receba uma string e inicialize a data
    def __init__(self, nome, data, ehferiado):
        self.nome = nome
        lista = data.split("/")
        self.dia = int(lista[0])
        self.mes = int(lista[1])
        self.ano = int(lista[2])
        self.ehferiado = ehferiado

    def ToString(self):
        lista = []
        lista.append(str(self.dia))
        lista.append(str(self.mes))
        lista.append(str(self.ano))
        data = '/'.join(lista)
        print(data)

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

    def __init__(self, nome, data):
        self.feriado = True
        super().__init__(nome, data, self.feriado)


class DatasComemorativas:
    def __init__(self):
        self.datas = []

    def adiciona_data(self, data):
        self.datas.append(data)
        print("=" * 30)
        print(f"Data adicionada = {data.nome}")
        print("=" * 30)

    def lista_datas(self):
        if self.datas == []:
            print("Lista vazia!")
        print("=" * 30)
        print("Lista de Datas comemorativas: ")

        for data in self.datas:
            print(f"{data.nome}: {data.dia}/{data.mes}/{data.ano}")

        print("=" * 30)

    def remove_data(self, nome):
        if nome in self.datas:
            self.datas.remove(nome)
            print("Data removida com sucesso!")

    def horas_nao_trabalhadas(self):
        cont = 0
        for data in self.datas:
            cont += 1

        print(f"{cont * 8}h não trabalhadas")
        print("=" * 30)


atual = MinhaData("atual", "06/12/2020", False)
natal = MinhaData("natal", "25/12/2020", True)
print(atual.compara(natal))

dados = DatasComemorativas()
dados.adiciona_data(natal)
dados.horas_nao_trabalhadas()

"""
SAÍDA = -1
SAÍDA = 8h
"""
