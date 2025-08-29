#atividade
import os
os.system ("cls")


login_salvo = "Marta"
senha_salva = "123"


login = input("Digite o seu login: ")
senha = input("Digite a sua senha: ")


if login == login_salvo and senha == senha_salva:
    print ("seja bem vindo!")
else: 
    print ("login ou senha inválidos")    
