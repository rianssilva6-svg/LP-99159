#atividade 

import os
os.system ("cls")

nome = input ("Digite seu nome: ")
idade = float(input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print ("voto opcional")
else:
    print ("voto obrigatorio")    
