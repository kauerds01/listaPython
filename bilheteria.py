#Aluno1: Padronizar o nome do filme--
def formatar(nome):
    return nome.upper()
#Aluno2: verificador de idade--
def verificar_idade(idade):
    if idade >= 18:
        return "Autorizado"
    else:
        return "Não autorizado"
#Aluno3: Mensagem de retorno
def gerar_mensagem(status):
    if status == "Autorizado":
        return "tenha uma otíma sessão!"
    else:
        return "Sentimos, mas você não tem idade minima."
#Aluno4: Execução do Algoritmo
filme_entrada = input("Digite o filme escolhido ")
idade_entrada = int(input("Digite sua Idade: "))
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(f"\nFilme:{nome_final}")
print(f"Status:{status_acesso}")
print(f"Mensagem:{mensagem}")