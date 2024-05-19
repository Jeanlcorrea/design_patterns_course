from abc import ABC, abstractmethod


class ItinerarioTemplate(ABC):
    def criar_itinerario(self):
        self.reservar_transporte()
        self.reservar_hospedagem()
        self.adicionar_atividades()
        self.enviar_confirmacao()

    @abstractmethod
    def reservar_transporte(self):
        pass

    @abstractmethod
    def reservar_hospedagem(self):
        pass

    @abstractmethod
    def adicionar_atividades(self):
        pass

    def enviar_confirmacao(self):
        print("Enviando e-mail de confirmação para o cliente.")


class ViagemPraia(ItinerarioTemplate):
    def reservar_transporte(self):
        print("Reservando voo para o destino de praia.")

    def reservar_hospedagem(self):
        print("Reservando hospedagem em resort na praia.")

    def adicionar_atividades(self):
        print("Adicionando atividades: snorkeling, vôlei de praia e cruzeiro ao pôr do sol.")


class ViagemMontanha(ItinerarioTemplate):
    def reservar_transporte(self):
        print("Reservando trem para o destino de montanha.")

    def reservar_hospedagem(self):
        print("Reservando hospedagem em cabana na montanha.")

    def adicionar_atividades(self):
        print("Adicionando atividades: trilhas, ciclismo de montanha e observação de estrelas.")


def main():
    print("Criando itinerário para Viagem à Praia...")
    viagem_praia = ViagemPraia()
    viagem_praia.criar_itinerario()

    print("\nCriando itinerário para Viagem à Montanha...")
    viagem_montanha = ViagemMontanha()
    viagem_montanha.criar_itinerario()


if __name__ == "__main__":
    main()
