# FACADE
class GerenciamentoEventos:

    def __init__(self):
        self.salao = SalaoFestas()
        self.florista = Florista()
        self.comida = Restaurante()
        self.musica = Banda()

    def organizar(self):
        print('GerenciamentoEventos :: Vou organizar com todo mundo! \n \n')

        self.salao.agendar()

        self.florista.arranjar_flores()

        self.comida.preparar()

        self.musica.montar_palco()


# SUBSISTEMA
class SalaoFestas:

    def __init__(self):
        print('SalaoFestas :: Agendando o salão de festas para o casamento...')

    @staticmethod
    def _esta_disponivel():
        print('SalaoFestas :: Este salão de festas está disponível? ')
        return True

    def agendar(self):
        if self._esta_disponivel():
            print('SalaoFestas :: Agendamento do salão realizado! \n')


# SUBSISTEMA 2
class Florista:

    def __init__(self):
        print('Florista :: Flores para um evento? ')

    @staticmethod
    def arranjar_flores():
        print('Florista: Rosas, Margaridas e Lírios serão usados... \n')


# SUBSISTEMA 3
class Restaurante:
    def __init__(self):
        print('Restaurante :: Comida para eventos...')

    @staticmethod
    def preparar():
        print('Restaurante :: Comida chinesa e brasileira serão servidas...\n')


# SUBSISTEMA 4
class Banda:
    def __init__(self):
        print('Banda :: Arranjos musicais para o evento')

    @staticmethod
    def montar_palco():
        print('Banda :: Preparando o palco para tocar jazz e rock no evento.\n')


# CLIENTE
class Cliente:
    def __init__(self):
        print('Cliente :: Uau! Preparando meu casamento')

    @staticmethod
    def contrata_gerente_eventos():
        print('Cliente :: Vou contratar um gerente de eventos\n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi simples organizar este evento com o Façade')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()
