import os
os.system ("cls")



print ("Bem vindo ao seu sistema de compras tudo por R$ 50")



# 1 Passo - Entrada 

compra =input("Digite o que deseja comprar:")
qtade =int(input("Digite a quantidade que deseja:"))
valor = 50
sdesconto = qtade * valor

# 2 Passo - Processamento 

if qtade <=5:
    desconto = sdesconto * 0.02
    total = sdesconto - desconto
    print ("Seu item",compra,"ficou no valor de:",total, "Com desconto de 2 porcento")

    
elif qtade >5 and qtade <=10:
    desconto = sdesconto * 0.03
    total = sdesconto - desconto
    print ("Seu item",compra,"ficou no valor de:",total, "Com desconto de 3 porcento")

elif qtade >10:
    desconto = sdesconto * 0.10
    total = sdesconto - desconto
    print ("Seu item",compra,"ficou no valor de:",total, "Com desconto de 10 porcento")

input ("Pressione <ENTER> para sair")    

