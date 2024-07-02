import os

os.system ("cls")


print ("Bem vindo ao descobrindo se valor é POSITIVO, NEGATIVO ou NEUTRO")

# 1 Passo - Entrada 

numero = int(input("Digite o numero:"))

# 2 Passo - Processamento/Saida

if numero > 0:
    print("O número é POSITIVO")


elif numero  < 0:
    print("O número é NEGATIVO")




else:
    print("O número é NEUTRO")



input ("Pressione <ENTER> para sair")    