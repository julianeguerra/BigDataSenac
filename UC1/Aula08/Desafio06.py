import random

def rolar_dado(lados):
    numero_lados = random.randint(1, lados)
    return numero_lados

print('Rolar para o Ataque (d20). Aperte Enter para rolar.')
input()
ataque = rolar_dado(20)
print('Rolar para o Dano (d8). Aperte Enter para rolar.')
input()
dano = rolar_dado(8)
print(f'Seu ataque é {ataque}.')
print(f'Seu dano é {dano}.')

