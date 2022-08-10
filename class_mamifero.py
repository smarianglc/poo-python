from class_animal import Animal
import string

class Mamifero(Animal):
    def __init__(self, nome: string, comprimento: float, numPatas: int, cor: string, ambiente: string, velocidade: float, alimento: string):
        super().__init__(nome, comprimento, numPatas, cor, ambiente, velocidade)
        self.__alimento = alimento

    @property
    def alimento(self):
        return self.__alimento

    @alimento.setter
    def alimento(self, alimento):
        self.__alimento = alimento

    def __repr__(self) -> str:
        return  f'{self.nome} | comprimento: {self.comprimento} | Numero de patas: {self.numPatas} | Cor: {self.cor} |  Ambiente: {self.ambiente} | Velocidade: {self.velocidade} |Alimento: {self.alimento}' 