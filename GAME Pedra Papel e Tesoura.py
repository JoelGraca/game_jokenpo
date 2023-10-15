from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou \033[1;36m{}\033[m'.format(itens[computador]))
print('Jogador jogou \033[1;33m{}\033[m'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:  # computador jogou PEDRA
    if jogador == 0:
        print('\033[1;36mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;31;46m>>>JOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;35mCOMPUTADOR VENCE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif computador == 1:  # computador jogou PAPEL
    if jogador == 0:
        print('\033[1;35mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;36mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;31;46m>>>JOGADOR VENCE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
elif computador == 2:  # computador jogou TESOURA
    if jogador == 0:
        print('\033[1;31;46m>>>JOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[1;35mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[1;36mEMPATE!\033[m')
    else:
        print('\033[1;31mJOGADA INVÁLIDA!\033[m')
