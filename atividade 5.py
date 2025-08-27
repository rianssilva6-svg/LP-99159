# teste
import os
os.system

n1 = float (input ("Digite o primeiro número: \n"))
n2 = float (input ("Digite o segundo número: \n"))



soma = n1 + n2
produto = n1 * n2
média = soma / 2
menor_valor = min(n1,n2)
maior_valor = max(n1,n2)


print (f"A soma: {soma}\n")
print (f"O produto: {produto}\n")
print (f"A Média: {média}\n")
print (f"Menor valor é: {menor_valor}\n")
print (f"Maior valor é: {maior_valor}\n")

if média == n1:
    print("São números iguais!!")
else:
    print("Não são números iguais!!")



