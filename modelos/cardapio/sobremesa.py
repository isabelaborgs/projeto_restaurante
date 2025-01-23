from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, descricao, tamanho):
        super().__init__(nome, preco)
        self._descricao = descricao
        self._tamanho = tamanho
    
    def __str__(self):
        return f'{super().__str__()} | {self._descricao.ljust(30)} | {self._tamanho}'

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.1)
        self._preco = round(self._preco, 2)