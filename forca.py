# Programa 01 -  Jogo da forca

secreta = input('Digite a palavra secreta:\n\n> ')
palavras = ''
digitadas = []
chances = 5

while True:
    if chances == 0:
      print('Você perdeu! ')
      exit()
  
    letra = input('Digite uma letra:\n\n> ')
    if len(letra) > 1:
      print('Você não digitou uma letra.\n\n')
      continue
    digitadas.append(letra)
    if letra not in secreta:
      chances -= 1
      print('\nA letra não existe na palavra secreta')
    else:
      print(f'{letra} Existe na palavra!')

    for reservador in secreta:

      if reservador in digitadas:
        palavras += reservador
      else:
        palavras += '*'

    if palavras == secreta:
      print('Você ganhou! Parabéns! A palavra secreta era', secreta)
      exit()

    
      # Exibição:

    print(f'\n\nPalavra: {palavras}')
    print(f'Chances: {chances}')
    palavras = ''

    #---------------------------------------

    


