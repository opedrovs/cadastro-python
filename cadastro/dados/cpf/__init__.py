from cadastro.decoracao.cores import *


def validaCPF(cpfEnviado):
    cpfLimpo = cpfEnviado.replace('.', '').replace('-', '')
    return cpfLimpo


def geraDigito(cpfSemDigitos):
    total = 0
    reverso = len(cpfSemDigitos) + 1

    for stringNumerica in cpfSemDigitos:
        total += reverso * int(stringNumerica)
        reverso -= 1

    digito = 11 - (total % 11)
    return str(digito) if digito <= 9 else '0'


def geraNovoCpf(cpfLimpo):
    cpfSemDigitos = cpfLimpo[0:-2]
    digito1 = geraDigito(cpfSemDigitos)
    digito2 = geraDigito(cpfSemDigitos + digito1)
    novoCPF = cpfSemDigitos + digito1 + digito2
    return novoCPF


def isSequencia(cpfLimpo):
    sequencia = cpfLimpo in cpfLimpo[0] * 11
    return sequencia


def valida(cpfLimpo):
    if not cpfLimpo.isnumeric():
        return False
    if len(cpfLimpo) != 11:
        return False
    if isSequencia(cpfLimpo):
        return False
    novoCPF = geraNovoCpf(cpfLimpo)

    return novoCPF == cpfLimpo


def leiaCPF(msg):
    while True:
        cpf = str(input(msg)).strip()
        cpfLimpo = validaCPF(cpf)
        if valida(cpfLimpo):
            return cpf
        else:
            print(f'{vermelho}CPF inválido! Digite um válido!{limpar}')
