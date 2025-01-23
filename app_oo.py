from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

#Cadastrando o restaurante
restaurante_praca = Restaurante('Restaurante na Praça', 'Gourmet')
#Cadastrando os itens
bebida_suco = Bebida('Suco de Maracujá', 5.00, '500ml')
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade!')
bebida_refrigerante = Bebida('Coca-cola', 10.00, '1L')
prato_biscoito = Prato('Biscoito', 2.00, 'Biscoito macio e quentinho!')
bebida_cerveja = Bebida('Spaten', 7.00, 'Long Neck')
sobremesa_bolo = Sobremesa('Bolo de chocolate', 10.00, 'Bolo no pote delicioso!', 'Pequeno')
#Adicionando os itens cadastrados ao cardápio
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_refrigerante)
restaurante_praca.adicionar_no_cardapio(prato_biscoito)
restaurante_praca.adicionar_no_cardapio(bebida_cerveja)
restaurante_praca.adicionar_no_cardapio(sobremesa_bolo)
#Aplicando descontos
bebida_cerveja.aplicar_desconto()
sobremesa_bolo.aplicar_desconto()
prato_biscoito.aplicar_desconto()

def main():
    restaurante_praca.cardapio

if __name__ == '__main__':
    main()