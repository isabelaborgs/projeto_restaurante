from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

class Restaurante:
    '''Representa um restaurante e suas caracterísitcas'''
    restaurantes = []
    
    def __init__(self, nome, categoria):
        '''Inicializa uma instância de um restaurante.
        
        Parâmetros:
        - nome (str): o nome do restaurante
        - categoria (str): a categoria do restaurante
        '''
        #avaliação e ativo não são colocados como parâmetro porque não é uma informação a ser inserida ao instanciar objeto
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'''Nome: {self._nome}
Categoria: {self._categoria}
Avaliação: {self.media_avaliacoes}
Status: {self.ativo}
'''

    #def __str__(self):
        '''Retorna uma representação em string do restaurante'''
    #    return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes cadastrados e suas características'''
        print(f'{'NOME DO RESTAURANTE'.ljust(30)} | {'CATEGORIA'.ljust(30)} | {'AVALIAÇÃO'.ljust(30)} | STATUS')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(30)} | {restaurante._categoria.ljust(30)} | {str(restaurante.media_avaliacoes).ljust(30)} | {restaurante.ativo}')

    @property
    def ativo(self):
        '''Retorna um símbolo indicando se um restaurante está ativo ou não'''
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        '''Alterna estado do restaurante entre ativo e inativo'''
        self._ativo = not self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        '''Registra uma avaliação para um restaurante
        
        Parâmetros:
        - cliente (str): nome do cliente que fez a avaliação
        - nota (float): nota atribuída pelo cliente ao restaurante, de 0 a 5
        '''
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações de um restaurante'''
        if not self._avaliacao:
            return 'Sem avaliações'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media    
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def cardapio(self):
        print(f'CARDÁPIO DO RESTAURANTE "{self._nome.upper()}"\n')
        bebidas = [item for item in self._cardapio if isinstance(item, Bebida)]
        pratos = [item for item in self._cardapio if isinstance(item, Prato)]
        sobremesas = [item for item in self._cardapio if isinstance(item, Sobremesa)]
        print('Bebidas')
        for i, bebida in enumerate(bebidas, start = 1):
            print(f'{i} - {bebida}')
        print('\nPratos')
        for i, prato in enumerate(pratos, start = 1):
            print(f'{i} - {prato}')
        print('\nSobremesas')
        for i, sobremesa in enumerate(sobremesas, start = 1):
            print(f'{i} - {sobremesa}')