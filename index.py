import random # importa o módulo random para gerar números pseudo-aleatórios

# minhas frases armazenadas em uma lista
frases = ["Seja paciente e confie no processo, você não come o fruto no mesmo dia que planta a semente.","Que você consiga todas as coisas que ninguém sabe que você está tentando.","A disciplina vai te levar a lugares onde a motivação não chega.","Não precisa ser muito, só precisa ser constante.","Se você tentou e falhou, parabéns. Tem gente que nem tenta.", "Aquele que não estuda pelo futuro que quer, terá que aceitar o futuro que vier.", "O grande problema dos garotos é que noventa por cento deles são meio que qualquer coisa. Se a gente vestisse e higienizasse os caras direitinho, se conseguisse colocar uma postura decente neles, fazer com que ouvissem as garotas e não fossem uns idiotas, eles seriam totalmente aceitáveis.", "Nas melhores conversas, nem nos lembramos do que falamos, só nos lembramos da sensação.","Qualquer um pode olhar para você, mas é muito raro encontrar quem veja o mesmo mundo que o seu.","Fazer as coisas nunca é tão bom quanto imaginá-las.","Os homens embarcam nos trens, mas já não sabem mais o que procuram.","A vida é uma tempestade, meu amigo. Um dia você está tomando sol e no dia seguinte o mar te lança contra as rochas. O que faz de você um homem é o que você faz quando a tempestade vem.", "O mais feliz dos felizes é aquele que faz os outros felizes.", "É preciso que eu suporte duas ou três larvas se quiser conhecer as borboletas.", "É bem mais difícil julgar a si mesmo do que julgar os outros. Se consegues fazer um bom julgamento de ti, és um verdadeiro sábio.", "Faça algo hoje pelo o qual o seu eu do futuro irá lhe agradecer.", "Não deseje que as coisas sejam mais fáceis; deseje que você seja melhor.", "Jamais considere seus estudos como uma obrigação, mas como uma oportunidade invejável para aprender a conhecer a influência libertadora da beleza do reino do espírito, para seu próprio prazer pessoal e para proveito da comunidade à qual seu futuro trabalho pertencer.", "Conhecimento não é aquilo que você sabe, mas o que você faz com o aquilo que você sabe.", "A verdadeira motivação vem de realização, desenvolvimento pessoal, satisfação no trabalho e reconhecimento.", "Se quiser ser feliz, amarre-se a uma meta, não a pessoas ou a coisas.", "Grandes obras são executadas não pela força mas pela perseverança.", "É melhor você tentar algo, vê-lo não funcionar e aprender com isso, do que não fazer nada.", "Você nunca sabe que resultados virão da sua ação, mas se você nunca fizer nada, não existirão resultados.", "Suba o primeiro degrau com fé. Não é necessário que você veja toda a escada. Apenas dê o primeiro passo.", "As raízes dos estudos são amargas, mas seus frutos são doces.", "A força vem de fazer coisas que você achava que não podia.", "Você atingirá o sucesso quando apresentar com orgulho as cicatrizes que adquiriu ao longo da sua jornada.", "Eu não estou aqui para ser mediano, estou aqui para ser o melhor;", "Há cinco degraus para se alcançar a sabedoria: calar, ouvir, lembrar, sair, estudar.",'''Não sei… Se a vida é curta
Ou longa demais pra nós,
Mas sei que nada do que vivemos
Tem sentido, se não tocamos o coração das pessoas.

Muitas vezes basta ser:
Colo que acolhe,
Braço que envolve,
Palavra que conforta,
Silêncio que respeita,
Alegria que contagia,
Lágrima que corre,
Olhar que acaricia,
Desejo que sacia,
Amor que promove.

E isso não é coisa de outro mundo,
É o que dá sentido à vida.

É o que faz com que ela
Não seja nem curta,
Nem longa demais,
Mas que seja intensa,
Verdadeira, pura… Enquanto durar''', '''Errei mais de 9.000 cestas e perdi quase 300 jogos.
Em 26 diferentes finais de partidas fui encarregado de jogar a bola que venceria o jogo... e falhei. Eu tenho uma história repleta de falhas e fracassos em minha vida.
E é exatamente por isso que sou um sucesso.''','''Não te deixes destruir…
Ajuntando novas pedras
e construindo novos poemas.
Recria tua vida, sempre, sempre.
Remove pedras e planta roseiras e faz doces. Recomeça.
Faz de tua vida mesquinha
um poema.
E viverás no coração dos jovens
e na memória das gerações que hão de vir.
Esta fonte é para uso de todos os sedentos.
Toma a tua parte.
Vem a estas páginas
e não entraves seu uso
aos que têm sede.''', '''A felicidade aparece para aqueles que choram.
Para aqueles que se machucam.
Para aqueles que buscam e tentam sempre.''', '''Na convivência, o tempo não importa.
Se for um minuto, uma hora, uma vida.
O que importa é o que ficou deste minuto,
desta hora, desta vida…
Lembra que o que importa
… é tudo que semeares colherás.
Por isso, marca a tua passagem,
deixa algo de ti,…
do teu minuto,
da tua hora,
do teu dia,
da tua vida.”''', '''O tempo é algo que não volta atrás.
Por isso plante seu jardim e decore sua alma,
Ao invés de esperar que alguém lhe traga flores.''', '''Em certa ocasião alguém perguntou a Galileu Galilei:
- Quantos anos tens?
- Oito ou dez, respondeu Galileu, em evidente contradição com a sua barba branca.
E logo explicou:
Tenho, na verdade, os anos que me restam de vida, porque os já vividos não os tenho mais.''', '''Se você achar que eu estou derrotado
Saiba que ainda estão rolando os dados...
Porque o tempo, o tempo não para!''']

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