def menu_principal():
    entrada = 's'
    while entrada == 's':
        print("\n=== MENU PRINCIPAL ===\n")
        print("1 - Menu Adm")
        print("2 - Operador")
        print("3 - Sair")
        opc = input("Digite uma opção: ")
        if opc == '1':
            menu_adm()
        elif opc == '2':
            print('2')
        elif opc == '3':
            entrada = 'n'
        else:
            print('Opção Invalida!')

def menu_adm():
    entrada = 's'
    while entrada == 's':
        print("\n=== MENU ADM ===\n")
        print('1 - Cadastrar Produto')
        print('2 - Listar Produtos')
        print('3 - Excluir Produtos')
        print('4 - Modificar Produto')
        print('5 - Retornar ao Menu')
        opc = input("Digite uma opção: ")
        if opc == '1':
            cadastrar_produto()
        elif opc == '2':
            listar_produtos()
        elif opc == '3':
            codigo = input("Digite o código do produto que deseja excluir: ")
            excluir_produtos(codigo)
        elif opc == '4':
            codigo = input("Digite o código do produto que deseja modificar: ")
            modificar_produto(codigo)
        elif opc == '5':
            entrada = 'n'

def cadastrar_produto():
    codigo = buscar_cod()
    descricao = input("Digite a descrição do produto: ")
    valor_u = input("Digite o valor do produto: ")
    produto = f'{codigo}, {descricao}, {valor_u}\n'
    with open("Produtos.txt", 'a') as arquivo:
        arquivo.write(produto)

def buscar_cod():
    codigos = []
    with open("Produtos.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        if not dados: # Verificando se o arquivo.txt não esta vazio.
            return '100'
        for linha in dados:
            partes = linha.strip().split(', ')
            if partes and partes[0].isdigit(): # Verificando se o valor do código é válido e se nao está vazio.
                codigos.append(int(partes[0]))
            else:
                return '100'
        
        for i in range(100, max(codigos) + 2):
            if i not in codigos:
                return str(i)
            
        return str(max(codigos)+ 1 )

def listar_produtos():
    with open("Produtos.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        for i in dados:
            print(i)

def excluir_produtos(codigo):
    produto_encontrado = False
    outros_produtos = []
    with open("Produtos.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        for linha in dados:
            partes = linha.strip().split(', ')
            if partes and partes[0] == codigo:
                produto_encontrado = True
            else:
                outros_produtos.append(linha)
            
    if produto_encontrado:
        print("Produto Excluido!")

    with open('Produtos.txt', 'w') as arquivo:
        arquivo.writelines(outros_produtos)

def modificar_produto(codigo):
    produto_encontrado = False
    outros_produtos = []
    with open("Produtos.txt", 'r') as arquivo:
        dados = arquivo.readlines()
        for linha in dados:
            partes = linha.strip().split(', ')
            if partes and partes[0] == codigo:
                produto_encontrado = True
            else:
                outros_produtos.append(linha)

    if produto_encontrado:
        print("Produto Encontrado!")

    nova_descricao = input("Digite a nova descrição: ")
    novo_valor = input("Digite o novo valor: ")
    novo_produto = f'{codigo}, {nova_descricao}, {novo_valor}\n'
    with open("Produtos.txt", 'w') as arquivo:
        arquivo.write(novo_produto)
        arquivo.writelines(outros_produtos)

menu_principal()





