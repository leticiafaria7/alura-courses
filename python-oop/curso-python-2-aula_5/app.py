from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# restaurantes
restaurante_praca = Restaurante('praça', 'Gourmet')

# bebidas e pratos
bebida_suco = Bebida('Suco de Melancia', 5.00, 'grande')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')

# aplicar desconto
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()

# adicionar no cardapio
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()