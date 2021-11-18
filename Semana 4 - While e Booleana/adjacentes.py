numero = int((input('Digite um numero: ')))
tamanho = len(str(numero))
adjacentes = False

while tamanho != 1 and not adjacentes:
  numero1 = numero % 100
  anterior = numero1 // 10
  resto = numero % 10
  if resto == anterior:
    adjacentes = True
  numero = numero // 10
  tamanho = len(str(numero))

if adjacentes:
  print('Existem numeros adjacentes')
else:
  print('Não existem numeros adjacentes')