from cadastro.dados.menus import *

# Programa principal

soma = media = totmul = 0

menu()
while True:
    nome = str(input('Nome completo: '))
    idade = leiaInt('Idade: ')

    while True:
        sexo = str(input(f'Sexo: [{azul}M{limpar}/{roxo}F{limpar}] ')).strip().upper()
        if sexo == 'M' or sexo == 'F':
            break
        print(f'{vermelho}ERRO: Por favor, responda apenas M ou F.{limpar}')

    cpf = leiaCPF('CPF: ')

    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['sexo'] = sexo

    pessoa['cpf'] = cpf
    dados.append(pessoa.copy())
    pessoa.clear()

    while True:
        resp = str(input(f'Quer continuar? [{verde}S{limpar}/{vermelho}N{limpar}] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
        print(f'{vermelho}ERRO: Responda apenas S ou N.{limpar}')
    linha()

    if resp == 'N':
        break

while True:
    print('Escolha uma das opções abaixo:')
    print(f'''{amarelo}[ 1 ] {azul}Ver estatísticas
{amarelo}[ 2 ] {azul}Ver detalhes
{amarelo}[ 3 ] {azul}Adicionar pessoa
{amarelo}[ 4 ] {azul}Sair do programa{limpar}''')
    try:
        opc = int(input(f'{verde}->{limpar} Sua Opção: '))
    except:
        print(f'{vermelho}Opção inválida! Tente novamente!{limpar}')
        linha()
    else:
        if opc == 1:
            verEstatisticas()
        elif opc == 2:
            verDetalhes()
        elif opc == 3:
            adicionarPessoa()
        elif opc == 4:
            break
menuFinal()
