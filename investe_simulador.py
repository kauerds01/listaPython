#Simulador de Investimento---
deposito_mensal = 50
total = 0 
for mes in range(1,20):
    total = total + deposito_mensal
    print(f"Mês {mes}: Saldo total= R${total}")
print(f"Ao final de 6 meses seu deposito foi de: R${total}")