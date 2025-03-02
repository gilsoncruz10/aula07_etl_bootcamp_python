# 1) Ler o arquivo CSV e carregar os dados.

# 2) Processar os dados em um dicionário, onde:
#    a chave é a categoria, e
#    o valor é uma lista de dicionários, 
#    cada um contendo informações do produto (Produto, Quantidade, Venda).
# 3) Calcular o total de vendas (Quantidade * Venda) por categoria.

# a. ler csv
# b. processar dados
# c. calcular vendas
# d. exibir resultados

path_arquivo = "vendas.csv"

import csv
def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários,
    garantindo que os nomes das colunas não tenham espaços extras.
    """
    with open(nome_do_arquivo_csv, mode= "r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)

        # Limpar espaços dos nomes das colunas
        leitor.fieldnames = [nome.strip() for nome in leitor.fieldnames]

        lista = [linha for linha in leitor]
    return lista


# vendas_itens: list[dict]
# vendas_itens = ler_csv(path_arquivo)

# print(vendas_itens)


def filtrar_produtos_entregues(lista: list[dict]) -> list[dict]:
    """
    Funcao que filtra produtos onde "entregue = True"
    """
    lista_de_produtos_entregues = []
    for produto in lista:
        #if produto.get("entregue") == "True":
        if produto.get("entregue", "").strip().lower() == "true":
            lista_de_produtos_entregues.append(produto)
    return lista_de_produtos_entregues

lista_de_produtos = ler_csv(path_arquivo)
lista_entregues = filtrar_produtos_entregues(lista_de_produtos)
print("lista de produtos vendidos: ", lista_de_produtos)
print("lista de produtos entregues: ", lista_entregues)
