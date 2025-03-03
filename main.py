from etl import ler_csv, filtrar_produtos_entregues, somar_os_precos_da_lista

path_arquivo = "vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
lista_entregues = filtrar_produtos_entregues(lista_de_produtos)
valor_dos_produtos_entregues = somar_os_precos_da_lista(lista_entregues)

print("lista de produtos vendidos: ", lista_de_produtos)
print("lista de produtos entregues: ", lista_entregues)
print("valor total dos produtos entregues: R$", valor_dos_produtos_entregues)