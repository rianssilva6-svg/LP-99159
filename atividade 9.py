#atividade 9

import os
os.system ("cls")

nome = input ("Digite seu nome: ")

print ("\n")

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

soma = n1 + n2
média = soma / 2

print ("\n")

print (f"A média do aluno é: {média}")

print ("\n")

if média < 4:
    conceito = "E"
elif média < 6:
    concetio = "D"    
elif média < 7.5:
    conceito = "C"
elif média < 9:
    conceito = "B"       
elif média <=10:
    conceito = "A"     
else: 
    conceito = "valor inválido"

if média <6:
    print(f"{nome}, você foi reprovado, seu conceito foi {conceito}") 
else:
    print(f"{nome}, você foi aprovado, seu conceito foi {conceito}")       