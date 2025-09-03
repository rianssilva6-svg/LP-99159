#atividade

import os
os.system ("cls")

print ("===Calendário===")

print("\n")

print ("Mês de Janeiro")
print ("Mês de Fevereiro")
print ("Mês de Março")
print ("Mês de Abril")
print ("Mês de Maio")
print ("Mês de Junho")
print ("Mês de Julho")
print ("Mês de Agosto")
print ("Mês de Setembro")
print ("Mês de Outubro")
print ("Mês de Novembro")
print ("Mês de Dezembro")

print ("\n")

mês = int(input("Digite o n° do mês: "))

match mês:
    case 1:
        print ("Mês de Janeiro")
    case 2:
        print ("Mês de Fevereiro")    
    case 3:
        print ("Mês de Março")
    case 4:
        print ("Mês de Abril")
    case 5:
        print ("Mês de Maio")
    case 6:
        print ("Mês de Junho")
    case 7:
        print ("Mês de Julho")
    case 8:
        print ("Mês de Agosto")
    case 9: 
        print ("Mês de Setembro")
    case 10:
        print ("Mês de Outubro")
    case 11:
        print ("Mês de Novembro")
    case 12:
        print ("Mês de Dezembro")
    case _:
        print ("Número do mês inválido")                                            


