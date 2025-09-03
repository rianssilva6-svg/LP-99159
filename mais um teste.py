#atividade

import os
os.system ("cls")

valor_do_produto = float(input("Digite o valor do produto: R$ "))
print ("formas de pagamento: ")
print ("1 - pagamento a vista")
print ("2 - pagamento parcelado")

forma_de_pagamento = int(input("Digite a forma de pagamento (1 ou 2): "))

match forma_de_pagamento:
    case 1:
        desconto = valor_do_produto * 0.10
        total = valor_do_produto - desconto
        print("\nResumo do pagamento á vista: ")
        print (f"Valor do produto: R$ {valor_do_produto:.2f}")
        print (f"Forma de pagamento: á vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print (f"Total a pagar: R$ {total:.2f}")
    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (até 6): "))
        if parcelas > 6 or parcelas < 1:
            print ("Quantidade de parcelas invalidas. Tente novamente")
        valor_parcelado = valor_do_produto / parcelas
        print("\nResumo do pagamento à prazo:")
        print(f"Valor do produto: R$ {valor_do_produto:.2f}")
        print(f"Forma de pagamento: à prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor por parcela: R$ {valor_parcelado:.2f}")
        print(f"Total à prazo: R$ {valor_do_produto:.2f}")           