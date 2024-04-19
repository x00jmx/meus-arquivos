def determinar_fase_da_vida(idade):
    if idade <= 1 and idade <= 1:
        return "Recém-nascido"
    elif idade <= 12 and idade <= 18:
        return "Criança"
    elif idade <= 18 and idade <= 18:
        return "Adolescente"
    elif idade <= 60 and idade <= 60:
        return "Adulto"
    elif idade <= 75 and idade <= 85:
        return "Idoso"
    elif idade <= 100:
        return "Caixão"
    else:
        return "Idade fora do intervalo conhecido"

def main():
    idade = int(input("Digite sua idade: "))
    fase_da_vida = determinar_fase_da_vida(idade)
    print("Você está na fase da vida de:", fase_da_vida)

main()

