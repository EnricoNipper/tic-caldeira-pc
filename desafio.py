#Função para mostrar o menu de opções
def exibir_menu():
    print("Menu de Opções:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Pesquisar produtos")
    print("4. Sair do programa")

# Função para adicionar um produto
def adicionar_produto(lista_produtos, id_atual):
    nome = input("Digite o nome do produto: ")
    unidade = input("Digite a unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ")

    unidades_validas = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    while unidade not in unidades_validas:
        print("Unidade inválida. Tente novamente.")
        unidade = input("Digite a unidade de medida (Quilograma, Grama, Litro, Mililitro, Unidade, Metro, Centímetro): ")

    try:
        quantidade = float(input("Digite a quantidade: "))
    except ValueError:
        print("Quantidade inválida. Definindo quantidade como 0.")
        quantidade = 0.0

    descricao = input("Digite a descrição do produto: ")

    produto = {
        'ID': id_atual,
        'Nome': nome,
        'Unidade': unidade,
        'Quantidade': quantidade,
        'Descrição': descricao
    }

    lista_produtos[id_atual] = produto
    print(f"Produto '{nome}' adicionado com sucesso.")

    return id_atual + 1  # Incrementar ID para o próximo produto

# Função para remover um produto
def remover_produto(lista_produtos):
    id_produto = input("Digite o ID do produto que deseja remover: ")

    if id_produto in lista_produtos:
        del lista_produtos[id_produto]
        print(f"Produto com ID '{id_produto}' removido com sucesso.")
    else:
        print("ID do produto não encontrado.")

# Função para pesquisar produtos
def pesquisar_produtos(lista_produtos):
    termo_pesquisa = input("Digite o nome ou parte do nome do produto para pesquisa: ").lower()
    encontrados = [produto for produto in lista_produtos.values() if termo_pesquisa in produto['Nome'].lower()]

    if encontrados:
        print(f"\nProdutos encontrados ({len(encontrados)}):")
        for produto in encontrados:
            print(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Unidade: {produto['Unidade']}, Quantidade: {produto['Quantidade']}, Descrição: {produto['Descrição']}")
    else:
        print("Nenhum produto encontrado.")

# Função para listar todos os produtos
def listar_produtos(lista_produtos):
    if lista_produtos:
        print("Lista de Produtos:")
        for produto in lista_produtos.values():
            print(f"ID: {produto['ID']}, Nome: {produto['Nome']}, Unidade: {produto['Unidade']}, Quantidade: {produto['Quantidade']}, Descrição: {produto['Descrição']}")
    else:
        print("A lista de produtos está vazia.")

def main():
    lista_produtos = {}
    id_atual = 1  # Inicializar o ID com 1

    while True:
        listar_produtos(lista_produtos)
        exibir_menu()

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            id_atual = adicionar_produto(lista_produtos, id_atual)
        elif opcao == '2':
            remover_produto(lista_produtos)
        elif opcao == '3':
            pesquisar_produtos(lista_produtos)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()