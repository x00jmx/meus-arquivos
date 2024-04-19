def saudacao():
    print("olá")
    print("mundo")
    
saudacao()

def imprime_nome(nome):
    print(f"nome: {nome}")
    
imprime_nome("Heitor")
imprime_nome("gabriella")
imprime_nome("mateuséviado")

def soma_dois_numeros(valor1, valor2):
    soma = valor1 + valor2
    return soma

valor_soma = soma_dois_numeros(32,15)
print(valor_soma)
print(soma_dois_numeros(50, 10))

def soma10(n):
    return n + 10

print(soma10(4))
print(soma10(5))

def media(a, b, c):
    return ( a+b+c) / 3

print(media(5,2,3))

def melhores_alunos(alun1, alun2, alun3):
    print(f"os melhores alunos do sesi são {alun1}, {alun2}, {alun3}")
    return(alun1,alun2,alun3)

def cad_pessoas(nome,idade, endereço):
    pessoa = nome,idade,endereço
    
    return pessoa
nome = input("digite o nome da pessoa:")
idade = int(input("digite a idade de pessoa:"))
endereço = input("digite o endereço da pessoa:")



def minha_funcao():
    x=10
    print(x)
    
    minha_funcao()
    print(x)