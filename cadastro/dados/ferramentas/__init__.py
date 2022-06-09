from cadastro.decoracao.cores import *


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'{vermelho}\nUsuário preferiu não digitar o valor!{limpar}')
            return 0
        except:
            print(f'{vermelho}ERRO: Digite um valor válido!{limpar}')
        else:
            num = int(n)
            return num


def formatarNum(num):
    return f'{num:.2f}'
