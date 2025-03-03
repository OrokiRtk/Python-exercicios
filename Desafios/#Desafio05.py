#dissecando uma variável
valor = input('Digite um valor: ')
print(f"Tipo primitivo: {type(valor)}" )
print(f'É númerico: {valor.isnumeric()}')
print(f'É alfabético: {valor.isalpha()}')
print(f'É alfanúmerico:{valor.isalnum()}')
print(f'Está em letras maiúsculas?{valor.isupper()}')
print(f'Está em letras minúsculas? {valor.islower()}')
print(f'Está capitalizada? {valor.istitle()}')
