import random
elementos = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
comprimento = int(input("Insira o comprimento da senha"))
senha = ""
for i in range(comprimento):
    senha += random.choice(elementos)
print(senha)