while True:
try:
nota = float(input('Insira uma nota entre 0 e 10: '))
if 0 <= nota <= 10: break
else:
print('Nota inválida. Insira uma nota entre 0 e 10.')
except ValueError:
print('Valor inválido. Insira um número.')

print(f'A nota informada foi: {nota}')