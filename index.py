#Mensagem de boas-vindas
print('Bem-vindo(a) ao açaí é vida - Alessandra de Souza Oliveira')
#Apresentação do cardápio
print('--------------------Cardápio----------------------')
print('------| Tamanho | Cupuaçu (CP)| Açaí (AC) |-------')
print('------|    P    |   R$ 10,00  |  R$ 12,00 |-------')
print('------|    M    |   R$ 15,00  |  R$ 17,00 |-------')
print('------|    G    |   R$ 29,00  |  R$ 21,00 |-------')
print('--------------------------------------------------')
#Escolha do sabor e tamanho

total = 0
while True:
  sabor = input('Escolha o sabor (CP/AC): ')
  sabor = sabor.upper()
  if sabor != 'CP' and sabor != 'AC':
    print('O sabor não existe, tente novamente!')
    continue

  tamanho = input('Escolha o tamanho (P/M/G): ')
  tamanho = tamanho.upper()
  if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
    print('O tamanho não existe, tente novamente!')
    continue

#Definição do sabor e tamanho do açaí e cupuaçu
  if sabor == 'CP' and tamanho == 'P':
    print('CUPUAÇU tamanho P: R$ 10,00')
    total = total + 10
  elif sabor == 'CP' and tamanho == 'M':
    print('CUPUAÇU tamanho M: R$ 15,00')
    total = total + 15
  elif sabor == 'CP' and tamanho == 'G':
    print('CUPUAÇU tamanho G: R$ 29,00')
    total = total + 29
  elif sabor == 'AC' and tamanho == 'P':
    print('AÇAÍ tamanho P: R$ 12,00')
    total = total + 12
  elif sabor == 'AC' and tamanho == 'M':
    print('AÇAÍ tamanho M: R$ 17,00')
    total = total + 17
  elif sabor == 'AC' and tamanho == 'G':
    print('AÇAÍ tamanho G: R$ 21,00')
    total = total + 21

#Continuação e finalização do pedido
  continuar = input('Gostaria de mais alguma coisa? (S/N)')
  continuar = continuar.upper()
  if continuar == 'S':
    continue

  else:
    print(f'Valor total do pedido R$ {total:.2f}')
    print('Obrigada pela preferência, volte sempre!')
    break