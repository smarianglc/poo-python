import random
from robo import Robo

class RoboMedico(Robo):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.poder_de_cura = round(random.random(),2)

    def curar (self, outro:'Robo'):
        if self.vida > outro.vida:
            outro.vida = 1
        else:
            print('Nivel da vida do médico é inferior')

    def __repr__(self):
        return super().__repr__()        

