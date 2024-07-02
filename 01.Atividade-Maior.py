import os
os.system("cls")



print ("Bem vindo ao descobrindo qual número é Maior ou Menor")

# 1 Passo - Entrada

maior = float(input("Digite o primeiro número:"))
menor = float(input("Digite o segundo número:"))

# 2 Passo - Processamento/Saida

if maior > menor:
    print ("O maior é:",maior,"e o menor valor é:", menor)

elif menor > maior:
    print ("O menor é:",menor,"e o maior valor é:", maior) 

elif maior == menor:
    print ("Os números são iguais")    


input ("Pressione <ENTER> para sair")    

