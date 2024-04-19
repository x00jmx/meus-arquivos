nome="josivaldo"
print(nome[::-1])

nome="josivaldo"
print(len(nome)) 


for letra in "brasil":
    print(letra)

for i in range(5):
    print(i)

soma = 0
for n in range(1, 11):
    soma += n
print (soma)

#primeiro desafio
palavra = input("Digite uma palavra: ")

vogais = 'aeiouAEIOU'
num_vogais = 0
num_consoantes = 0


for letra in palavra:
        if letra in vogais:
            num_vogais += 1
        else:
            num_consoantes += 1

print("Número de vogais:", num_vogais)
print("Número de consoantes:", num_consoantes)

#segundo desafio 
