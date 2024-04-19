nome = input("Digite o nome do cliente: ")
cpf = input("Digite o CPF do cliente: ")
salario = float(input("Digite o salário do cliente: "))
emprego = input("O cliente possui emprego? (s/n): ").lower() == 's'
casa_propria = input("O cliente possui casa própria? (s/n): ").lower() == 's'
negativado = input("O cliente está negativado? (s/n): ").lower() == 's'
salario_declarado = float(input("Digite o salário declarado pelo cliente: "))

if not negativado and emprego and salario > 0 and casa_propria and salario * 1.5 >= salario_declarado:
    print("Crédito aprovado para o cliente", nome)
else:
    print("Crédito negado para o cliente", nome)
jooj