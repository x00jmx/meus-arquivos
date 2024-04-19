
respostas = [0] * 7

while True:
    resposta = int(input("Digite a resposta (0 a 6, 0 para encerrar): "))
    

    if 0 <= resposta <= 6:
        respostas[resposta] += 1
    elif resposta == 0:
        break
    else:
        print("Resposta inválida. Digite novamente.")

total_respostas = sum(respostas)
percentuais = [round((valor / total_respostas) * 100, 2) for valor in respostas]

vencedor = percentuais.index(max(percentuais))

print("\nResultados da enquete:")
for i in range(1, 7):
    print(f"{i}- {percentuais[i]:.2f}%")

print(f"\nO vencedor da enquete é o Sistema Operacional {vencedor} com {percentuais[vencedor]:.2f}%.")



