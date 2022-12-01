import random
#CLASSE BASE 
class Robo: 
    nivel_critico = 0.60
    #METODO INIT: inicialiazando os atributos
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__vida = round(random.random(),2)

    @property
    def nome(self):
        return self.__nome

    @property
    def getVida(self):
        return self.__vida

    @getVida.setter
    def vida(self, vida: float):
        if vida > 1.0:
            vida = 1.0
        elif vida <= 0.00:
            vida = 0.01
        self.__vida = vida

   # def __add__(self, outro:'Robo'):
    #    return  type(self)(f'{self.nome}+{outro.nome}') 

    def __add__(self, outro):
        nomeA = self.__nome.split("-")[0]
        nomeB = outro.__nome.split("-")[0]
        return type(self)(f'{nomeA}-{nomeB}')

    def precisa_de_medico (self):
        if self.vida < self.nivel_critico:
            return True
        else:
            return False
    
    #METODO REPR: retorna os atributos da classe
    def __repr__(self):
        return f'{self.__nome}, {self.__vida}'     

