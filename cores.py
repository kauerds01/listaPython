# Criando a lista de cores

cores = ["Roxo", "Azul", "Vermelho"]

# Exibindo o tamanho total da lista

total = len(cores)

print(f"A lista possui {total} cores.")

#ponto 2

def aplicar_desconto(preco):

    valor_final = preco * 0.90

    return valor_final
 
valor_inicial = float(input("Digite o preço do produto: "))
preco_final = aplicar_desconto(valor_inicial)
print(f"O valor do seu produto com desconto é {preco_final}")

#Q3

idade = int(input("Digite sua idade: "))



if idade >=18 :

    print("Acesso Liberado")

else:

    print("Acesso Negado")