import string
from class_animal import Animal

class Peixe(Animal):
    def __init__(self, nome: string, comprimento: float, numPatas: int, cor: string, ambiente: string, velocidade: float, caract: string):
        super().__init__(nome, comprimento, numPatas, cor, ambiente, velocidade)
        self.__caract = caract

    @property
    def caract(self):
        return self.__caract

    @caract.setter
    def caract(self, caract):
        self.__caract = caract

    def __repr__(self) -> str:
        return f'{self.nome} | comprimento: {self.comprimento} | Numero de pata: {self.numPatas} | Cor: {self.cor} |  Ambiente: {self.ambiente} | Velocidade: {self.velocidade} | caracteristica: {self.caract}'