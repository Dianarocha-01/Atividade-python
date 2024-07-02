import os
os.system("cls")



# 1 Passo - Entrada

print ("Bem vindo a Calculadora")


v1 = int(input("Informe o primeiro valor:"))
v2 = int(input("Informe o segundo valor:"))

operacao = int(input("Digite o número correspondente a operação que deseja realizar \n 1 - SOMA \n 2 - ADIÇAO  \n 3 - MULTIPLICAÇÃO \n 4 - DIVISÃO \n "))


if operacao == 1:
    soma = v1 + v2
    r1 = soma
    print ("Seu resultado de soma:",soma)


elif operacao == 2:
    adicao = v1 - v2
    r2 = adicao
    print ("Seu resultado de adição é :",adicao)

elif operacao == 3:
    multiplicacao = v1 * v2
    r3 = multiplicacao
    print ("Seu resultado de multiplicação é:",multiplicacao)

elif operacao == 4:
    divisao = v1 / v2
    r4 = divisao
    print ("Seu resultado de divisão é:",divisao)

    
input ("Pressione <ENTER> para sair")      
