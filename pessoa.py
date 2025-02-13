class Pessoa:
    def __init__(self, nome, data_nasc, codigo, salario=0, estudando=True, trabalhando=False, nivel=1):
        self.nome = nome
        self.data_nasc = data_nasc
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = salario
        self.nivel = nivel
        print('init', self.trabalhando)


    def apresentar(self):
        print(f'Me chamo {self.nome},\n'
              f'Nasci em {self.data_nasc},\n'
              f'{'trabalhando' if self.trabalhando else "não trabalha" }\n'
              f'{'Estuda' if self.estudando else 'Não estuda'}\n'
              f'meu salário é {self.salario:.2f}\n'
              f'nivel {self.nivel}'
              f'meu código é {self.codigo}')

        print('-*-'*10)

    def comecar_trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            print(f'{self.nome} agora está trabalhando')
            self.salario = 100
            if self.estudando:
                salario = self.salario
                self.salario = salario + (salario / 10)
                print('aumento de 10% pq estuda')
            else:
                print('nenhum aumento pq n estuda')
        else:
            print('opa ja trabalha ja')


    def comecar_estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f'{self.nome} agora está estudando')
            if self.trabalhando:
                salario = self.salario
                self.salario = salario + (salario / 10)
                print('aumento de 10% pq estuda')
            else:
                print('nenhum aumento pq nem recebe')
        else:
            self.nivel += 1
            print(f'evoliu 1 nivel {self.nivel}')
            if self.trabalhando:
                salario = self.salario
                self.salario = salario + (salario / 10)
                print('aumento de MAIS 10% pq estudou dnv')

    def parar_estudar(self):
        if not self.estudando:
            if self.nivel > 0:
                self.nivel -= 1
            print('ja n estuda')
        else:
            self.estudando = False
            print(f'{self.nome} agora n estuda')
            if self.trabalhando:
                self.salario = 100
    def parar_trabalhar(self):
        if not self.trabalhando:
            print('ja n trabalha')
        else:
            self.trabalhando = False
            print(f'{self.nome} agora n trabalha')
            self.salario = 0

p1 = Pessoa('Pedro Silva', '20/03/2001', 1)
p2 = Pessoa('João Rocha', '27/11/1999', 2)
p3 = Pessoa('Mr. Pycharm', '18/01/2005', 3)
p4 = Pessoa('Mr. codigo', '29/08/2014', 4)
p5 = Pessoa('Luciano Wokwi', '18/06/2009', 5)
# lista_pessoas = [p1, p2, p3, p4, p5]
# for p in lista_pessoas:
#     p.apresentar()

# p1.apresentar()
# p1.parar_estudar()
# p1.comecar_trabalhar()
# p1.apresentar()
# p1.comecar_estudar()
# p1.apresentar()
# p1.parar_trabalhar()
# p1.apresentar()
# p1.comecar_trabalhar()
# p1.apresentar()
# p1.comecar_estudar()
# p1.apresentar()

p1.apresentar()
p1.comecar_estudar()
p1.apresentar()
p1.comecar_trabalhar()
p1.apresentar()