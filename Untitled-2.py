

valor1 = float(input("Insira o primeiro número: "))
valor2 = float(input("Insira o segundo número: "))

soma = valor1 + valor2 
print(soma)



nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média das notas é: {media}")



metros= float (input('digite o valor em metros'))

converte=metros * 100

print(converte)



import math

raio = float(input("Insira o raio do círculo: "))

area = math.pi * raio**2

print(f"A área do círculo é: {area}")



lado = float(input("Digite o comprimento do lado do quadrado: "))
area = lado ** 2
area_dobrada = area * 2
print(f"A área do quadrado é: {area:.2f}")

print(f"A área dobrada é: {area_dobrada:.2f}")



fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"A temperatura em Celsius é: {celsius:.2f}")



int1 = int(input('Digite um número inteiro:\n'))
int2 = int(input('Digite outro número inteiro:\n'))
float = float(input('Digite um número com vírgula:\n'))
float = float ** 3
float = round(float,2)

print('O produto do dobro do primeiro com metade do segundo é:',(int1 * 2) * (int2/2))

print('A soma do triplo do primeiro com o terceiro é:',(3*int1) + float)

print('O terceiro elevado ao cubo é:',float)


while True:
nota = float(input('Insira uma nota entre 0 e 10: '))
    if 0 <= nota <= 10: 

    break

    else:

    print('Valor inválido. Insira um número.')

print(f'A nota informada foi: {nota}')