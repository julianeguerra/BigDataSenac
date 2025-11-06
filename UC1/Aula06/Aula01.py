# lista01=['Juliane', 28, 28.6, True, None, 'Maria']
# print(lista01)
# print(type(lista01))
# print(lista01[2])

# for i in lista01:
#     print(i, ':', type(i))

lista02=[
    'Lavar louça',
    'Ir ao mercado',
    'Lavar banheiro',
    'Tirar poeira',
    'Lavar quintal']
lista02_pets = lista02.copy()
lista02_pets.append('Dar banho no dog')
lista02_pets.append('Limpar areia dos gatos')
lista02_pets.insert(5,'Ir ao veterinário')
# lista02.pop(5)
# print(lista02)
# print(lista02[1])
# print(lista02[1][6:13])
# print(lista02[1][6:])
# print(lista02[1][:6])
# print(lista02[1][6:],lista02[4][6:])
lista02_pets.remove('Ir ao veterinário')

print(lista02_pets)