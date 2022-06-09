from cadastro.dados.cpf import *
from cadastro.dados.ferramentas import *
from cadastro.decoracao.cores import *

dados = []
pessoa = {}
soma = media = totmul = 0


def linha():
    print(f'{amarelo}-{limpar}' * 40)


def menu():
    linha()
    print(f'{azul}Cadastro Pessoas'.center(48))
    linha()


def verEstatisticasMenu():
    linha()
    print(f'{azul}Estatísticas Pessoas'.center(50))
    linha()


def verEstatisticas():
    soma = totmul = 0
    verEstatisticasMenu()
    if len(dados) == 1:
        print(f'Temos {amarelo}{len(dados)}{limpar} pessoa cadastrada.')
    else:
        print(f'Temos {amarelo}{len(dados)}{limpar} pessoas cadastradas.')

    for pessoa in dados:
        soma += pessoa["idade"]
    media = soma / len(dados)
    print(f'A média de idade do grupo é de {verde}{formatarNum(media)}{limpar} anos.')

    for pessoa in dados:
        if pessoa['idade'] < 21 and pessoa['sexo'] == 'F':
            totmul += 1
    if totmul == 1:
        print(f'Ao todo, temos {amarelo}{totmul}{limpar} mulher com menos de 21 anos.')
    else:
        print(f'Ao todo, temos {amarelo}{totmul}{limpar} mulheres com menos de 21 anos.')

    print(f'As pessoas acima da média de idade são: ', end='')
    for pessoa in dados:
        if pessoa["idade"] > media:
            print(f'[{azul}{pessoa["nome"]}{limpar}] ', end='')
    print()
    linha()


def verDetalhesMenu():
    linha()
    print(f'{azul}Detalhes Informações'.center(48))
    linha()


def verDetalhes():
    verDetalhesMenu()
    print(f'{"Cód.":<4}', f'{"Nome":<18}', f'{"Idade":<8}', f'{"Sexo":<5}', f'{"CPF"}')
    for pos, pessoa in enumerate(dados):
        print(f'{pos:<4}', f'{pessoa["nome"]:<18}', f'{pessoa["idade"]:<8}', f'{pessoa["sexo"]:<5}', f'{pessoa["cpf"]}')
    linha()


def adicionarPessoaMenu():
    linha()
    print(f'{azul}Adicionar Pessoa'.center(52))
    linha()


def adicionarPessoa():
    adicionarPessoaMenu()
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
    print(f'{pessoa["nome"]} adicionado com sucesso!')
    dados.append(pessoa.copy())
    pessoa.clear()
    linha()


def menuFinal():
    linha()
    print(f'{azul}<<< {amarelo}FIM DO PROGRAMA! {azul}>>>{limpar}'.center(64))
    linha()
