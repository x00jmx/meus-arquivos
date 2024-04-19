clientes = []

# Adicionando informações dos clientes
while True:
    nome = input("Digite o nome do cliente (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
    
    cpf = input("Digite o CPF do cliente: ")
    negativado = input("O cliente está negativado? (sim/não): ").lower() == 'sim'
    emprego = input("O cliente tem emprego? (sim/não): ").lower() == 'sim'
    salario = float(input("Digite o salário do cliente: "))
    casa_propria = input("O cliente possui casa própria? (sim/não): ").lower() == 'sim'

    cliente = {"nome": nome, "cpf": cpf, "negativado": negativado, "emprego": emprego, "salario": salario, "casa_propria": casa_propria}
    clientes.append(cliente)

# CPF do cliente a verificar
cpf_cliente_verificar = input("Digite o CPF do cliente para verificar a aprovação de crédito: ")

# Verificando a aprovação de crédito para o cliente
for cliente in clientes:
    if cliente["cpf"] == cpf_cliente_verificar:
        if not cliente["negativado"]:
            if cliente["emprego"] and cliente["casa_propria"]:
                if cliente["salario"] * 1.5 <= cliente["salario"]:
                    print("Crédito aprovado para o cliente com CPF", cpf_cliente_verificar)
                else:
                    print("Crédito não aprovado para o cliente com CPF", cpf_cliente_verificar)
            else:
                print("Crédito não aprovado para o cliente com CPF", cpf_cliente_verificar)
        else:
            print("Crédito não aprovado para o cliente com CPF", cpf_cliente_verificar)