# Cálculo do IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# Coleta de informações do usuário
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Cálculo do imposto
imposto = calcular_imposto(peso, altura)

# Exibição do relatório
print("Olá", nome + "!")
print("Seja muito bem vindo!")
print("Você tem", idade, "anos")
print("Sua altura é", altura, "m")
print("Seu peso é", peso, "kg")
print("E o seu IMC é", imc)
