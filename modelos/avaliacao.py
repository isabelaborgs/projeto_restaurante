class Avaliacao:
    '''Representa dados que compõem avaliação'''

    def __init__(self, cliente, nota):
        '''Inicializa nova instância de avaliação
        
        Parâmetros:
        - cliente (str): nome do cliente que fez a avaliação
        - nota (float): nota atribuída pelo cliente ao restaurante
        '''
        self._cliente = cliente
        self._nota = nota
                                                    