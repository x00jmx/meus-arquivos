import modularização

def calculadora():
    
    while True:
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
        operacao = input("Operação (+, -, *, /): ")
        if operacao == "s1" :
            print(modularização.soma(n1,n2))
        elif operacao == "s1":
            print(modularização.subtracao(n1,n2))
        elif operacao == "m":
            print(modularização.multiplicacao(n1,n2))
        elif operacao == "d":
            print(modularização.divisao(n1,n2))
            break
        else:
            print("Operação inválida.")

calculadora()