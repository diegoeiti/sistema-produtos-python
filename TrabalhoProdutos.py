#Criando um programa para registrar produtos:
#Criando um arquivo.txt para evitar erros na hora da execução:
arquivo = open('Produtos.txt', 'a')
arquivo.close()
#Criando menu de adm e menu principal:

def menu_adm():
    entrada = 's'
    while entrada == 's':
        print("\n=== Menu Adm ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Modificar")
        print("4 - Excluir")
        print("5 - Retornar")
        opc = input("Digite uma opção: ")
        if opc == '1':
            cadastrar_produtos()
        elif opc == '2':
            listar_produtos()
        elif opc == '3':
            modificar_produtos()
        elif opc == '4':
            excluir_produto()  
        elif opc == '5':
            print("Retornando ao menu principal...")
            return
        else:
            print("Opção inválida!")

def menu_principal():
    entrada = 's'
    while entrada == 's':
        print("\n=== Menu Principal ===")
        print("1 - Modo Administrador")
        print('2 - Modo Operador(Vender Produtos)')
        print("3 - Encerrar Programa")
        opc = input("Digite uma opção: ")
        if opc == '1':
            menu_adm()
        elif opc == '2':
            operador()
        elif opc == '3':
            print("Encerrando o programa...")
            entrada = 'n'
        else:
            print("Opção inválida!")

# ========== FUNÇÕES DE CRUD ==========

# Criando a função de cadastrar produtos no arquivo txt:
def cadastrar_produtos():
    codigo = buscar_codigo()
    descricao = input("Digite a descrição do produto: ")
    valor_unitario = float(input("Digite o valor unitário do produto: "))
    quantidade_total = input("Digite a quantidade total do produto no estoque: ")
    produto = f'{codigo}; {descricao}; {valor_unitario}; {quantidade_total}\n'
    with open("Produtos.txt", 'a', encoding='utf-8') as arquivo:
        arquivo.write(produto)

# Criando função para listar produtos:
def listar_produtos():
    with open("Produtos.txt", 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
        for linha in dados:
            partes = linha.strip().split('; ')
            print(f'\nCódigo; {partes[0]}; Descrição; {partes[1]}; Valor; R${partes[2]} reais; Quantidade: {partes[3]}\n')

#Criando função para modificar produtos:
def modificar_produtos():
    listar_produtos()
    produto_encontrado = False # Criando uma flag para sinalizar se encontrou o produto.
    outro_produtos = []
    cod = input("Digite o código do produto que deseja modificar: ")
    with open("Produtos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split('; ')
            if partes and partes[0] == cod:
                produto_encontrado = True
            else:
                outro_produtos.append(linha)

    if produto_encontrado:
        print("Produto encontrado!")
    else:
        print("Produto não encontrado.")

    #Criando produto novo para substituir o antigo:
    nova_descricao = input("Digite a nova descrição do produto: ")
    novo_valor = input("Digite o novo valor do produto: ")
    nova_quantidade = input("Digite a nova quantidade do produto no estoque: ")
    novo_produto = f'{cod}; {nova_descricao}; {novo_valor}; {nova_quantidade}\n'
    #Escrevendo o produto novo no arquivo:
    with open("Produtos.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(outro_produtos)
        arquivo.write(novo_produto)

#Criando função para excluir produtos:
def excluir_produto():
    listar_produtos()
    produto_encontrado = False # Criando uma flag para sinalizar se encontrou o produto.
    outro_produtos = []
    cod = input("Digite o codigo do produto que deseja excluir: ")
    with open("Produtos.txt", 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split('; ')
            if partes and partes[0] == cod:
                produto_encontrado = True
            else:
                outro_produtos.append(linha)

    if produto_encontrado:
        print("Produto excluido com sucesso!")
    else:
        print("Produto não encontrado.")

    with open("Produtos.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(outro_produtos)


# Criando função para gerar código automaticamente:
def buscar_codigo():
    codigos = []
    with open('Produtos.txt', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split('; ')
            codigos.append(int(partes[0]))

        if not linhas:
            return '100'
    
        for i in range(100, max(codigos) + 2):
            if i not in codigos:
                return str(i)
            
        else:
            return str(max(codigos + 1))

#Criando função do moodo operador:
def operador():
    encontrado = False # Criando uma flag para sinalizar se encontrou o produto.
    nome_produto = ''
    quantidade_atual = 0
    novas_linhas = []
    valor_unitario = 0

    listar_produtos()
    nome_cliente = input("Digite o nome do cliente: ").strip()

    codigo_desejado = input("Digite o Codigo do produto que deseja vender: ")
    if not codigo_desejado.isdigit():
        print("Código inválido, digite apenas número.")
        return
    
    quantidade_desejada = int(input("Digite a quantidade desejada:  "))
    if quantidade_desejada <= 0:
        print("Valor inválido, digite um número acima de 0!")
        return
    
    with open("Produtos.txt", 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            partes = linha.strip().split('; ')
            if len(partes) == 4 and partes[0] == codigo_desejado:
                nome_produto = partes[1]
                quantidade_atual = int(partes[3])
                valor_unitario = float(partes[2])
                
                if quantidade_desejada > quantidade_atual:
                    print("Quantidade não disponível no estoque!")
                    return
                
                partes[3] = str(quantidade_atual - quantidade_desejada)
                encontrado = True

            novas_linhas.append('; '.join(partes)+'\n')
        
    with open("Produtos.txt", 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(novas_linhas)

    print("Venda Concluída!")
    print(f'Nome do cliente: {nome_cliente} // Quantidade vendida: {quantidade_desejada} // Nome do produto: {nome_produto} // Valor: R${quantidade_desejada * valor_unitario} reais')
    print("========= Lista Atualizada =========")
    listar_produtos()

menu_principal()
