from data import frases # importa a minha lista em outro file(arquivo)
import random # importa o módulo random para gerar números pseudo-aleatórios

while True:
  print(f"{'*'*70}")

  # esse while da ao user a opção de escolher de que forma ele quer acessar o elemento
  while True:
    print('Você quer exibir uma frase pelo índice, pelo modo aleatório ou saber a quantidade de frases?(0/1/2)')
    option = input()
    if option == '0':
      indice = int(input('\nDigite o índice abaixo:\n'))
      print(f'\n{frases[indice]}\n')
      break
    elif option == '1':
      print(f'\n{frases[random.randrange(0, len(frases))]}\n')
      break
    elif option == '2':
      print(f'\nO programa possui um total de {len(frases)} frases/poemas.\n')
      break
  
  # esse while pergunta ao user se ele quer continuar usando o programa
  while True:
    saida = input('Você deseja continuar?(S/n)\n').lower()
    if saida == 'n':
      print(f"{'*'*70}")
      break
    elif saida == 's':
      break
  if saida == 'n':
    break