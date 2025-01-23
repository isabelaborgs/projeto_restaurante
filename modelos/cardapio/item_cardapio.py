from abc import ABC, abstractmethod

class ItemCardapio:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    def __str__(self):
        return f'{self._nome.ljust(30)} | R${str(self._preco).ljust(30)}'
    
    @abstractmethod
    def aplicar_desconto(self):
        pass