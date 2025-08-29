#atividade

import os
os.system ("cls")

n1 = int(input("Digite o primeiro numero"))
n2 = int(input("Digite o segundo numero"))

calculo = input("Digite o operador para fazer o calculo: ")

match calculo:
    case "+":
        print(f"Numeros: {n1} e {n2}\noperador: {calculo}")