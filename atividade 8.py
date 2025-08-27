#atividade 8

import os
os.system ("cls")

nome = input ("Digite seu nome: ")
quantidade = int (input("Digite a quantidade de maçãs: "))
valor_das_maçãs = quantidade * 1.30

if valor_das_maçãs < 12:
    valor_das_maçãs = quantidade * 1.30
else:
    valor_das_maçãs = quantidade 

print (f"quantidade de maçãs: {quantidade}")
print (f"valor das maçãs: {valor_das_maçãs: .2f}")