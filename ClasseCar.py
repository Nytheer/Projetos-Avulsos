# Objetivo: criar uma classe para representar um carro.
# O carro terá alguns atributos: modelo, ano e velocidade
# e terá métodos: acelerar e imprimir as informações do carro.

class Carro:
    def __init__(self, model,ano):
        self.modelo = model
        self.ano = ano
        self.velocidade = 0
        
    def acelerar(self, aceleracao):
        self.velocidade += aceleracao
        print(f"o carro acelerou: {self.velocidade}")
        
    def imprimir_infos(self):
        print(f"modelo: {self.modelo} ano: {self.ano} com {self.velocidade} km")

Dados_Car = Carro("MCqueen", 2014)
Dados_Car.acelerar(20)
Dados_Car.imprimir_infos()
