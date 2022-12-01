from unicodedata import name
from class_animal import Animal
from class_mamifero import Mamifero
from class_peixe import Peixe

ob_camelo = Mamifero('Camelo',150, 4, 'Amerelo', 'Terra', 2.0, None)
print(ob_camelo)

ob_tubarao = Peixe('Tubarão', 300, 0,'Cinzento', 'Mar', 1.5, 'Barbatanas e Caudas')
print(ob_tubarao)

ob_ursoCanada = Mamifero('Urso-do-Canadá', 180, 4, 'vermelho', 'Terra', 0.5,'Mel')
print(ob_ursoCanada)

