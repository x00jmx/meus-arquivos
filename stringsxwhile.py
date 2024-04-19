
#primeiro desafio
palavra = input("Digite uma palavra: ")

vogais = 'aeiouAEIOU'
num_vogais = 0
for letra in palavra:
        if letra in vogais:
            num_vogais += 1
print("Número de vogais:", num_vogais)


#segundo desafio
dias_semana = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]

for _ in range(7):
    dia_digitado = input("Digite um dia da semana: ").lower()

    if dia_digitado in dias_semana:
        if dia_digitado in ["sábado", "domingo"]:
            print(f"{dia_digitado} não é um dia útil.")
        else:
            print(f"{dia_digitado} é um dia útil.")
            print(f"{dia_digitado}-feira")
    else:
        print("Por favor, digite um dia válido da semana.")


#terceiro desafio 
num = int(input("Digite um número inteiro positivo: "))

if num > 1: 

    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "não é um número primo")
            break
    else:
        print(num, "é um número primo")
else:
    print(num, "não é um número primo")
    

