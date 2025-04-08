#-*- coding: UTF-8 -*-

print("Digite a operação que eu lhe darei o resultado.")

def adicao(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    if valor2 != 0:
        return valor1 / valor2
    else:
        return "Erro: Divisão por zero!"

