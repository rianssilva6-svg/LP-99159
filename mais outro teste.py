#atividade

import os
os.system ("cls")

print ("====peso ideal====")
print ("1 - Masculino")
print ("2 - Feminino")

print ("\n")

gênero = input("Digite o seu gênero (1 ou 2): ")
Altura = float(input("Digite sua altura: "))

match gênero:
    case "1":
        gênero_altura = (72.7 * Altura) - 58
        print (f"Seu gênero é {gênero} = Masculino e seu peso ideal é {gênero_altura:.2f}kg")
    case "2":
        altura_genero = (62.1 * Altura) - 44.7 
        print (f"Seu gênero é {gênero} = Feminino e seu peso ideal é {altura_genero:.2f}kg")  
    case _:
        print ("Gênero inválido, tente novamente.")     



