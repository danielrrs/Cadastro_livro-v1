nome = []
autor = []
status = []
livros_armazenados = [nome, autor, status]

def salvar_em_txt():
    try:
        with open('livros.txt', 'w') as arquivo:
            for i in range(len(livros_armazenados[0])):
                arquivo.write(f"Nome: {livros_armazenados[0][i]}, Autor: {livros_armazenados[1][i]}, Status: {livros_armazenados[2][i]}\n")
        print("Dados salvos em livros.txt com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def remover_livro():
    global livros_armazenados 

    print("Livros disponíveis para remoção:")
    for i in range(len(livros_armazenados[0])):
        print(f"{i+1}. Nome: {livros_armazenados[0][i]}, Autor: {livros_armazenados[1][i]}, Status: {livros_armazenados[2][i]}")

    try:
        numero_livro = int(input("Digite o número do livro a ser removido: "))
        if 1 <= numero_livro <= len(livros_armazenados[0]):
            livro_removido = (
                livros_armazenados[0].pop(numero_livro - 1),
                livros_armazenados[1].pop(numero_livro - 1),
                livros_armazenados[2].pop(numero_livro - 1)
            )
            print(f"O livro '{livro_removido[0]}' de '{livro_removido[1]}' foi removido com sucesso.")
            salvar_em_txt()  # Adiciona a chamada para salvar após remover
        else:
            print("Número de livro inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número válido.")
        
    voltar_ao_menu()

def fazer_consulta():
    global livros_armazenados 

    print("Livros disponíveis para consulta:")
    for i in range(len(livros_armazenados[0])):
        print(f"{i+1}. Nome: {livros_armazenados[0][i]}, Autor: {livros_armazenados[1][i]}, Status: {livros_armazenados[2][i]}")

    voltar_ao_menu()

def adiciona_livro():
    n_nome = input("Digite o nome do livro: ")
    n_autor = input("Digite o autor: ")
    n_status = input("Digite o local:")
    novo_livro = n_nome, n_autor, n_status

    livros_armazenados[0].append(novo_livro[0])
    livros_armazenados[1].append(novo_livro[1])
    livros_armazenados[2].append(novo_livro[2])

    voltar_ao_menu()

def sair():
    salvar_em_txt()  # Adiciona a chamada para salvar antes de sair
    print("Adios")

def voltar_ao_menu():
    print("Pressione 1 para voltar ao menu ou 2 para fechar o programa")
    escolha = input()
    if escolha == '1':
        menu()
    else:
        print("Adeus")

def menu():
    print("Bem-vindo ao menu de escolha, escolha uma opção:")
    print("1 Adicionar livros")
    print("2 Consultar Livros")
    print("3 Remover Livros")
    print("4 Sair")

    escolha = input("Digite um número: ")

    if escolha == '1':
        adiciona_livro()
    elif escolha == '2':
        fazer_consulta()
    elif escolha == '3':
        remover_livro()
    elif escolha == '4':
        sair()
    else:
        print("Escolha inválida. Por favor, digite um número válido.")

menu()
