# Sistema de Gerenciamento de Estoque

estoque = {}
estoque_minimo = 5

def menu():
    print("\n==== MENU ====")
    print("1. Cadastrar Produto")
    print("2. Remover Produto")
    print("3. Editar Produto")
    print("4. Entrada de Produto")
    print("5. Saída de Produto")
    print("6. Consultar Produto")
    print("7. Relatório de Estoque")
    print("8. Relatório de Baixo Estoque")
    print("0. Sair")

def cadastrar_produto():
    id_prod = input("ID do produto: ")
    if id_prod in estoque:
        print("Produto já cadastrado.")
        return
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    try:
        quantidade = int(input("Quantidade em estoque: "))
        preco = float(input("Preço: "))
        estoque[id_prod] = {
            'nome': nome,
            'categoria': categoria,
            'quantidade': quantidade,
            'preco': preco
        }
        print("Produto cadastrado com sucesso.")
    except ValueError:
        print("Erro: entradas inválidas.")

def remover_produto():
    id_prod = input("ID do produto a remover: ")
    if id_prod in estoque:
        del estoque[id_prod]
        print("Produto removido.")
    else:
        print("Produto não encontrado.")

def editar_produto():
    id_prod = input("ID do produto a editar: ")
    if id_prod in estoque:
        nome = input("Novo nome: ")
        categoria = input("Nova categoria: ")
        try:
            quantidade = int(input("Nova quantidade: "))
            preco = float(input("Novo preço: "))
            estoque[id_prod].update({
                'nome': nome,
                'categoria': categoria,
                'quantidade': quantidade,
                'preco': preco
            })
            print("Produto atualizado.")
        except ValueError:
            print("Erro: entradas inválidas.")
    else:
        print("Produto não encontrado.")

def movimentar_estoque(entrada=True):
    id_prod = input("ID do produto: ")
    if id_prod in estoque:
        try:
            quantidade = int(input("Quantidade: "))
            if entrada:
                estoque[id_prod]['quantidade'] += quantidade
                print("Entrada registrada.")
            else:
                if quantidade <= estoque[id_prod]['quantidade']:
                    estoque[id_prod]['quantidade'] -= quantidade
                    print("Saída registrada.")
                else:
                    print("Erro: estoque insuficiente.")
        except ValueError:
            print("Erro: entrada inválida.")
    else:
        print("Produto não encontrado.")

def consultar_produto():
    opcao = input("Buscar por (1) Nome, (2) Categoria, (3) ID: ")
    termo = input("Digite o termo de busca: ").lower()
    encontrados = []
    for id_prod, dados in estoque.items():
        if (opcao == '1' and termo in dados['nome'].lower()) or \
           (opcao == '2' and termo in dados['categoria'].lower()) or \
           (opcao == '3' and termo == id_prod.lower()):
            encontrados.append((id_prod, dados))

    if encontrados:
        for id_prod, dados in encontrados:
            print(f"ID: {id_prod} | Nome: {dados['nome']} | Categoria: {dados['categoria']} | Quantidade: {dados['quantidade']} | Preço: R${dados['preco']:.2f}")
    else:
        print("Nenhum produto encontrado.")

def relatorio_estoque():
    print("\n--- Produtos em Estoque ---")
    for id_prod, dados in estoque.items():
        print(f"ID: {id_prod} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']} | Preço: R${dados['preco']:.2f}")

def relatorio_baixo_estoque():
    print("\n--- Produtos com Baixo Estoque ---")
    encontrados = False
    for id_prod, dados in estoque.items():
        if dados['quantidade'] < estoque_minimo:
            print(f"ID: {id_prod} | Nome: {dados['nome']} | Quantidade: {dados['quantidade']}")
            encontrados = True
    if not encontrados:
        print("Todos os produtos estão com estoque adequado.")

# Loop principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        cadastrar_produto()
    elif escolha == '2':
        remover_produto()
    elif escolha == '3':
        editar_produto()
    elif escolha == '4':
        movimentar_estoque(entrada=True)
    elif escolha == '5':
        movimentar_estoque(entrada=False)
    elif escolha == '6':
        consultar_produto()
    elif escolha == '7':
        relatorio_estoque()
    elif escolha == '8':
        relatorio_baixo_estoque()
    elif escolha == '0':
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")