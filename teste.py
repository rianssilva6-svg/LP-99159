#atividade

import os 
os.system ("cls")

print ("\n")

print ("===Seja bem vindo===")
print ("Cardápio")

print ("\n")

print ("""
codigo \t\t prato \t\t\t valor
  1\t\t Picanha \t\t R$25,00 
  2\t\t Lasanha \t\t R$20,00  
  3\t\t Strogonoff \t\t R$ 18,00           
  4\t\t Bife Acebolado \t R$ 15,00
  5\t\t Pão com ovo \t\t R$ 5,00        
""")

print ("\n")

pedido = input("Digite o numero do pedido: ")

match pedido: 
    case "1":
        print ("Você pediu uma picanha companheiro e o valor é R$25,00, agora faz o L")
    case "2":
        print ("Você escolheu lasanha, o valor é R$20,00")    
    case "3":
        print("Você pediu um strogonoff, o valor é R$18,00")
    case "4":
        print ("Você pediu um bife acebolado, o valor é R$15,00")
    case "5":
        print ("Você pediu pão com ovo, valor é R$ 5,00")            
    case _:
        print ("prato inválido, tente novamente!")    