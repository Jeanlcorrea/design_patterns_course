from abc import ABC, abstractmethod


# Assunto / Tópico / Sujeito
class EstacaoMeteorologica:
    """
        Enquanto o cliente configura o sistema inicialmente, é o sujeito que gerencia a comunicação com os observadores
        quando as condições monitoradas mudam. Isso ajuda a manter uma separação clara de responsabilidades no sistema,
        tornando-o mais flexível e extensível.
    """
    def __init__(self):
        self._observadores = []
        self._temperatura = None
        self._umidade = None
        self._pressao = None

    def adicionar_observador(self, observador):
        self._observadores.append(observador)

    def remover_observador(self, observador):
        self._observadores.remove(observador)

    def notificar_observadores(self):
        for observador in self._observadores:
            observador.atualizar(self._temperatura, self._umidade, self._pressao)

    def definir_medicoes(self, temperatura, umidade, pressao):
        self._temperatura = temperatura
        self._umidade = umidade
        self._pressao = pressao
        self.notificar_observadores()


# Interface Observer
class Observador(ABC):
    @abstractmethod
    def atualizar(self, temperatura, umidade, pressao):
        pass


# Observador A
class DisplayCondicoesAtuais(Observador):
    def atualizar(self, temperatura, umidade, pressao):
        print("Display de Condições Atuais:")
        print(f"Temperatura: {temperatura} C, Umidade: {umidade}%, Pressão: {pressao} hPa\n")


# Observador B
class RegistroLog(Observador):
    def atualizar(self, temperatura, umidade, pressao):
        print("Registrando no Log:")
        print(f"Temperatura: {temperatura} C, Umidade: {umidade}%, Pressão: {pressao} hPa\n")


# Observador C
class AlertaTemperatura(Observador):
    def atualizar(self, temperatura, umidade, pressao):
        if temperatura > 30:
            print("ALERTA DE TEMPERATURA!")
            print(f"Temperatura atual: {temperatura} C\n")


# Cliente
if __name__ == '__main__':
    estacao_meteorologica = EstacaoMeteorologica()

    display = DisplayCondicoesAtuais()
    log = RegistroLog()
    alerta = AlertaTemperatura()

    estacao_meteorologica.adicionar_observador(display)
    estacao_meteorologica.adicionar_observador(log)
    estacao_meteorologica.adicionar_observador(alerta)

    estacao_meteorologica.definir_medicoes(25, 60, 1013)  # Mudança de condições
