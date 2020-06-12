from function import *
import time
import getpass
while True:
    time.sleep(0.5)
    print('='*70)
    print(f'{"ENCODER CHECKPOINT":^70}')
    print('='*70)
    print('[1] para codificar nova inserção')
    print('[2] para visualizar inserções codificadas')
    print('[3] para visualizar inserções codificadas e decodificadas')
    print('[4] para sair')
    print('-'*70)
    resp = input('digite opçao: ')
    print('-'*70)
    if resp == '1':
        novaInsercao()
    elif resp == '2':
        print('mostrando inserções codificadas:')
        print()
        mostraItens()
    elif resp == '3':
        print('apenas administradores podem ver texto original. SENHA = checkpoint')
        senha = getpass.getpass('DIGITE SUA SENHA:')
        print()
        print('-'*70)
        if senha == 'checkpoint':
            print('mostrando inserções codificadas e texto original:')
            print()
            mostraItens(3)
        else:
            print('senha inválida')
    elif resp == '4':
        print('finish')
        break
    else:
        print('valor inválido, tente novamente')


    
