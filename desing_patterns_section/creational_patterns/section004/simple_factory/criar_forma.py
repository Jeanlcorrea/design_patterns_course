from abc import ABCMeta, abstractmethod
from math import pi


# Classe abstrata representando a interface das formas
class Forma(metaclass=ABCMeta):
    @abstractmethod
    def calcular_area(self):
        pass


# Classes concretas que implementam a interface Forma
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return pi * self.raio**2


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado**2


# Fábrica simples para criar objetos Forma
class FabricaFormas:
    def criar_forma(self, tipo, *args, **kwargs):
        if tipo == 'Circulo':
            return Circulo(*args, **kwargs)
        elif tipo == 'Quadrado':
            return Quadrado(*args, **kwargs)
        else:
            raise ValueError("Tipo de forma desconhecido")


# Cliente
if __name__ == '__main__':
    fabrica = FabricaFormas()

    tipo_forma = input("Qual forma você quer criar? [Circulo/Quadrado]: ")

    if tipo_forma:
        if tipo_forma == 'Circulo':
            raio = float(input("Digite o raio do círculo: "))
            forma = fabrica.criar_forma(tipo_forma, raio=raio)
        elif tipo_forma == 'Quadrado':
            lado = float(input("Digite o lado do quadrado: "))
            forma = fabrica.criar_forma(tipo_forma, lado=lado)
        else:
            print("Tipo de forma inválido.")
            forma = None
    else:
        # Se nenhum tipo for especificado, cria um círculo padrão com raio 1
        forma = fabrica.criar_forma('Circulo', raio=1)

    if forma:
        area = forma.calcular_area()
        print(f"A área da forma é: {area}")
