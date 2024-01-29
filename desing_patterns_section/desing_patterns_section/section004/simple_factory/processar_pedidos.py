from abc import ABCMeta, abstractmethod


# Classe abstrata representando a interface dos pedidos
class Pedido(metaclass=ABCMeta):
    @abstractmethod
    def preparar_ingrediente_principal(self):
        pass

    @abstractmethod
    def adicionar_acompanhamentos(self):
        pass

    @abstractmethod
    def cozinhar(self):
        pass

    def processar_pedido(self):
        # Método concreto com implementação padrão
        self.preparar_ingrediente_principal()
        self.adicionar_acompanhamentos()
        self.cozinhar()
        print("Pedido pronto e entregue ao cliente.")


# Classes concretas que implementam a interface Pedido
class PedidoPizza(Pedido):
    def preparar_ingrediente_principal(self):
        print("Preparando a massa de pizza.")

    def adicionar_acompanhamentos(self):
        print("Adicionando molho de tomate e queijo.")

    def cozinhar(self):
        print("Assando a pizza.")


class PedidoHamburguer(Pedido):
    def preparar_ingrediente_principal(self):
        print("Preparando o hambúrguer.")

    def adicionar_acompanhamentos(self):
        print("Adicionando alface, tomate e queijo.")

    def cozinhar(self):
        print("Grelhando o hambúrguer.")


# Fábrica simples para criar objetos Pedido
class FabricaPedidos:
    def criar_pedido(self, tipo):
        if tipo == 'Pizza':
            return PedidoPizza()
        elif tipo == 'Hamburguer':
            return PedidoHamburguer()
        else:
            raise ValueError("Tipo de pedido desconhecido")


# Cliente
if __name__ == '__main__':
    fabrica = FabricaPedidos()

    tipo_pedido = input("Qual pedido você deseja fazer? [Pizza/Hamburguer]: ")

    if tipo_pedido:
        pedido = fabrica.criar_pedido(tipo_pedido)
    else:
        # Se nenhum tipo for especificado, cria um pedido de pizza por padrão
        pedido = fabrica.criar_pedido('Pizza')

    pedido.processar_pedido()
