from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
from random import randint
from time import sleep

robos_normal = [Robo('Alberto-LI'), Robo('Ana-SL'), Robo('Cris-GO')]
robmed = [RoboMedico('Mateus'), RoboMedico('Debora'), RoboMedico('João')]
roblut = [RoboLutador('Jaqueline'), RoboLutador('Sara'), RoboLutador('Vitor')]

def curando(medico, paciente):
    print('CHAMANDO MÉDICO')
    print(f'{medico.nome} em ação!')
    print('-' * 30)
    sleep(2)
    if paciente.precisa_de_medico():
        if randint(0, 1) == 1:
            medico.curar(paciente)
            print(f'{medico.nome} cura {paciente.nome} | Vida: {paciente.vida}')
        else:
            print(f'{paciente.nome} não será curado!')
    else:
        print(f'{paciente.nome} não precisa de cura!({paciente.vida} maior que 0.100)')

print('======= 1° luta ==========')
print(f'{roblut[2].nome} vs {roblut[1].nome}')
print('-'*29)
sleep(2)

print('VIDAS INIADAS:')
print(f'{roblut[2]} | Poder: {roblut[2].poder}')
print(f'{roblut[1]} | Poder: {roblut[1].poder}')
print('-'*20)
sleep(5)

print(f'{roblut[2].nome} ATACA {roblut[1].nome}')
roblut[2].atacar(roblut[1])

curando(robmed[randint(0,2)], roblut[0])
sleep(5)
curando(robmed[randint(0,2)], roblut[1])
sleep(5)

input('Pressione ENTER para continuar')

print('============== 2° LUTA ============')
print(f'{roblut[0].nome} vs {robos_normal[0].nome}')
print('-'*29)
sleep(2)

print('Vidas iniciais:')
print(f'{roblut[0]} | Poder: {roblut[0].poder}')
print(f'{robos_normal[0]} | Poder: Não Possui')
print('-'*20)
sleep(5)

print(f'{roblut[0].nome} ATACA {robos_normal[0].nome}')
roblut[0].atacar(robos_normal[0])

curando([randint(0,2)], roblut[0])
sleep(5)
curando(robmed[randint(0,2)], robos_normal[0])

input('Pressione ENTER para continuar')

print('-'*30)
print('=========== CASAMENTOS ============')
print('-'*30)
print('Robo com Robo')
print(f'{robos_normal[0].nome} com {robos_normal[1].nome} nasce {robos_normal[0]+robos_normal[1]}')
print('\nRoboDeluta com Robo')
print(f'{roblut[2].nome} com {robos_normal[2].nome} nasce {roblut[2]+robos_normal[2]}')
print('\nRoboMedico com Robo')
print(f'{robmed[0].nome} com {robos_normal[1].nome} nasce {robmed[0]+robos_normal[1]}')
print('\nRoboDeLuta com RoboMedico')
print(f'{roblut[1].nome} com {robmed[2].nome} nasce {roblut[1]+robmed[2]}')