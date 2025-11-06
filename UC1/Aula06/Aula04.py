filme = {
    'nome': 'V for Vendetta',
    'ano': 2005,
    'genero': 'Ação',
    'faixa_etaria': 16
}
print(filme)
print(type(filme))

print(filme['ano'])

print(filme.keys())
print(filme.values())
print(len(filme))

filme['duracao']='13 min'
filme['genero']='Thriller/Drama'
print(filme)

filme.pop('duracao')
print(filme)