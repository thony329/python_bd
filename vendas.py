from conexao import conecta_db
from datetime import datetime
def menu_vendas (opcao):
    print("|-------------------------")
    print("|     Menu -> Vendas      ")
    print("--------------------------")
    print("|   1 - Consultar Vendas  ")
    print("|   2 - Inserir Vendas    ")
    print("|   3 - Sair              ")
    print("|-------------------------")
conexao = conecta_db()
while True:
    opcao = input("Escolha uma opcao :")
    if opcao == "1":
        consultar_vendas()
    elif opcao == "2":
        inserir_venda()
    elif opcao == "3":
        break
    else:
        print("Opcao Invalida< tente novamente")

def consultar_venda():
    print("Nao implemetado")


def inserir_venda():
   id_cliente = input("Digite o ID do Cliente")
   date_venda = datetime.now()
   numero = 0
   valor_venda = 0

    