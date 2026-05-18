print("Bem vindo a sua Tabuada Digital😁")
numero = int(input("Qual o número da tabuada que você deseja? "))
print(f"---Tabuda do {numero}---")
for i in range (1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")