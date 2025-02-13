class Onibus():
    def __init__(self, fabricante, modelo, ano, cor, quilometragem):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.quilometragem = quilometragem

    def exibir_info(self):
        print('-*-'*10)
        print(f' Fabricante: {self.fabricante}\n'
              f' Modelo: {self.modelo}\n'
              f' Ano: {self.ano}\n'
              f' Cor: {self.cor}\n'
              f' Quilometragem: {self.quilometragem} Km')
        print('-*-'*10)

    def acelerar(self):
        print(f'O {self.modelo} - {self.fabricante}, faz VRUUUUUMMM!!!1!!! ')

bus1 = Onibus('Volkswagen', 'Viaggio G7 900',
              2005, 'Azul', 35000)
bus2 = Onibus('Volvo', '9700 Grand S',
              2012, 'Amarelo', 15000)
lista_bus = [bus1, bus2]
for bus in lista_bus:
    bus.exibir_info()
