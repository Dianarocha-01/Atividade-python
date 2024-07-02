import os

os.system("cls")

print ("Bem vindo a escola APRENDER!")
print ("Vamos calcular suas aulas")

qtde_aula =int(input("Digite a quantidade de aula:"))
nivel =int(input("Digite o seu nivel para continuar!\n 1- Nivel 1 pressione 1 \n 2- Nivel 2 pressione 2 \n 3- Nivel 3 pressione 3 \n"))

if nivel == 1:
    n1 = 12
    valor = n1 * qtde_aula
    salario = valor
    print ("Seu o valor pelas suas aulas é:",salario)

elif nivel == 2:
    n2 = 17
    valor = n2 * qtde_aula
    salario = valor
    print ("Seu o valor pelas suas aulas é:",salario)


elif nivel == 3:
    n3 = 25
    valor = n3 * qtde_aula
    salario = valor
    print ("Seu o valor pelas suas aulas é:",salario)


else:
    print("Nivel digitado invalido")
    
input ("Pressione <ENTER> para sair")    

