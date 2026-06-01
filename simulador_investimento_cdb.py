#Simulador CDB 💸--
print("--Seja bem vindo ao seu simulador pessoal de investimentos😁--")
print("--O percentual de juros é calculado em cima da cota do CDB!--")
aporte = float(input("Quanto você irá investir por mês?"))
meses = int(input("Quantos meses você irá investir?"))
juros = 1.24/100
total = 0
for mes in range(1, meses +1):
    total = total + aporte
    total = total + (total*juros)
    print(f"Mês{mes}:Saldo total= R${total}")
print(f"Ao final de {meses} meses, você terá um valor de {total:.2f}")
#Kauê Rodrigues da Silva
