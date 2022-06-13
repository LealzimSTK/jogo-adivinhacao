"""

░██████╗████████╗██╗░░██╗  ░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░███╗░░██╗██╗░░░██╗
██╔════╝╚══██╔══╝██║░██╔╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗████╗░██║╚██╗░██╔╝
╚█████╗░░░░██║░░░█████═╝░  ██║░░╚═╝██║░░██║██╔████╔██║██████╔╝███████║██╔██╗██║░╚████╔╝░
░╚═══██╗░░░██║░░░██╔═██╗░  ██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██║██║╚████║░░╚██╔╝░░
██████╔╝░░░██║░░░██║░╚██╗  ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║░╚███║░░░██║░░░
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░
"""

import random  # Biblioteca 1
import time  # Biblioteca 2

print("\x1b[2J")  # Clear console

aleatorio = random.randint(0, 5)  # Gerar um número aleatório
print('{:^40}'.format('Adivinhe o número'))
print('-=-' * 13)  # Linha decorativa
print('Digite um número de 0 a 5')  # Print de alerta
print('-=-' * 13)  # Linha decorativa
user = int(input('> '))  # Número do Usuário
time.sleep(1)  # Espera
print('ANALISANDO...')  # Alerta de espera
time.sleep(2.7)  # Espera
if user == aleatorio:
    print('Você Ganhou!')  # Mostra se o número gerado é igual ao número do User
else:
    # Se o número for diferente o computador ganha
    print('O computador ganhou!')
    print('O número correto era {}'.format(
        aleatorio))  # Mostra o número correto
print('') # Pulo de uma linha
print('Deseja jogar de novo?') # Vai perguntar se o usuário quer jogar
user3 = input('>').upper().strip()[0] # Vai pedir a resposta do usuário
r = 'S' # Resposta padrão
while r == 'S': # Enquanto o usuário não ganhar do computador:
    aleatorio = random.randint(0, 5)
    print("\x1b[2J")  # Clear console
    print('{:^40}'.format('Adivinhe o número'))
    print('-=-' * 13)  # Linha decorativa
    print('Digite um número de 0 a 5')  # Print de alerta
    print('-=-' * 13)  # Linha decorativa
    user = int(input('> '))  # Número do Usuário
    time.sleep(1)  # Espera
    print('ANALISANDO...')  # Alerta de espera
    time.sleep(2.7)  # Espera
    if user == aleatorio:
        print('Você Ganhou!')  # Mostra se o número gerado é igual ao número do User
    else:
        # Se o número for diferente o computador ganha
        print('O computador ganhou!')
        print('O número correto era {}'.format(
            aleatorio))  # Mostra o número correto
    print('')
    r = input('Deseja jogar de novo?: ').upper().strip()[0] # Escolha do jogador
else:
    print('Jogo Finalizado') # Argumento Final
