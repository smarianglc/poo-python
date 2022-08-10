import string


class Animal:
    def __init__ (self, nome: string, comprimento: float, numPatas: int, cor: string, ambiente: string, velocidade: float):
        self.__nome = nome
        self.__comprimento = comprimento
        self.__numPatas = numPatas 
        self.__cor = cor 
        self.__ambiente = ambiente
        self.__velocidade = velocidade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def comprimento(self):
        return self.__comprimento

    @property
    def numPatas(self):
        return self.__numPatas
    
    @property
    def cor(self):
        return self.__cor

    @property
    def ambiente(self):
        return self.__ambiente

    @property
    def velocidade(self):
        return self.__velocidade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @comprimento.setter
    def comprimento(self, comprimento):
        self.__comprimento = comprimento

    @numPatas.setter
    def numPatas(self, numPata):
        self.__numPatas = numPata

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @ambiente.setter
    def ambiente(self, ambiente):
        self.__ambiente = ambiente

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    def __repr__(self) -> str:
        return f'{self.nome} | comprimento: {self.comprimento} | Numero de pata: {self.numPatas} | Cor: {self.cor} |  Ambiente: {self.ambiente} | Velocidade: {self.velocidade}' 
    
