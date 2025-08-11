def formatar_nome(nome):  
    return nome.strip().title()

def cadastrar_produtos():
    nome = input("Digite o nome do produto: ") 
    preco = float(input("Digite o preço do produto: "))
    categoria = input(" Digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)

def salvar_produtos(produto):
    with open("produto.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)   
    
def listar_produtos():
    try:
        with open("produtos.txt", "r", encoding="utf-8")as arquivos
        for linha in arquivos:
            nome, preco, categoria = linha.strip().split(";")
            print(f"Produtos: {nome} | Peço: r${preco} | categoria: {categoria}")
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.")