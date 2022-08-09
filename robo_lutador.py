from robo import Robo
import random

class RoboLutador(Robo):
    dano_maximo = 0.2

    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self.poder = round(random.uniform(self.dano_maximo, 1),2)

    def atacar (self, outro):
        vida = outro.vida * 1 - self.poder
        outro.vida = vida
        if str(type(outro)) == "<class '__main__.RoboLutador'>":  
           vida = self.vida * 1 - outro.poder
           self.vida= vida
    
    def __repr__(self):
        return super().__repr__()

r1 = RoboLutador('aline')
print(r1)
r2 = RoboLutador('ana')
print(r2)
r1.atacar(r2)
print(r1)
print(r2)




