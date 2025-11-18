import os

ARQUIVO_DADOS = "/dados/lista_nomes.txt"

def menu():
    print("\n--- MENU ---")
    print("1. Escrever novo nome")
    print("2. Ler nomes salvos")
    opcao = input("Escolha (1 ou 2): ")
    return opcao

def escrever():
    nome = input("Digite o nome para salvar: ")
    with open(ARQUIVO_DADOS, "a") as arquivo:
        arquivo.write(nome + "\n")
    print("Nome salvo com sucesso!")

def ler():
    if os.path.exists(ARQUIVO_DADOS):
        print("\n--- CONTEUDO DO ARQUIVO ---")
        with open(ARQUIVO_DADOS, "r") as arquivo:
            print(arquivo.read())
        print("---------------------------")
    else:
        print("O arquivo ainda nao existe. Adicione um nome primeiro.")

if __name__ == "__main__":
    if not os.path.exists("/dados"):
        os.makedirs("/dados")
        
    while True:
        escolha = menu()
        if escolha == "1":
            escrever()
        elif escolha == "2":
            ler()