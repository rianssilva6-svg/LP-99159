# atividade 3

import os
os.system ("cls")

n1 = float (input ("Digite a primeira nota: "))
n2 = float (input ("Digite a segunda nota: "))
n3 = float (input ("Digite a terceira nota: "))

soma = n1 + n2 + n3
média = soma / 3

print(f"soma: {soma}")
print(f"média: {média}")

if média > 7:
    print("aprovado acima de 7")
else:
    print ("reprovado abaixo de 7")  


