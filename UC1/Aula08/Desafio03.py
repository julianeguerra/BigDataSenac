def celsius_para_fahrenheit():
    temp_c = float(input('Insira a temperatura em Celsius: '))
    temp_f = (temp_c * 9/5) + 32
    print(f'{temp_c} em Fahrenheit é: {temp_f}.')


def fahrenheit_para_celsius():
    temp_f = float(input('Insira a temperatura em Fahrenheit: '))
    temp_c = (temp_f - 32) * 5/9
    print(f'{temp_f} em Celsius é: {temp_c}.')

def conversao():
    valor = float(input('Qual conversão você quer fazer? Digite 1 para C->F e 2 para F->C: '))
    if valor == 1:
        celsius_para_fahrenheit()
    elif valor == 2:
        fahrenheit_para_celsius()
    else:
        print('Insira 1 ou 2.')

conversao()