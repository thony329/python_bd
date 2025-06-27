from cliente  import menu_cliente
from categoria import menu_categoria
from produto import menu_produto
from usuario import menu_usuario, login 

from conexao import conecta_db

def menu_principal():
    print("----------------------------------------------")
    print("        Menu-> Programa                       ")
    print("----------------------------------------------")
    print("           1 - Cliente                        ")
    print("           2 - Categoria                      ")
    print("           3 - Produção                       ")
    print("           4 - Usuario                        ")
    print("           5 - Vendas                         ")
    print("           5 - Sair do Sistema                ")
    print("----------------------------------------------")

    while True:
        opcao = input("Escolha uma opção")

        if opcao == "1":
            menu_cliente()
        elif opcao == "2":
            menu_categoria("Categoria")
        elif opcao == "3":
           menu_produto()
        elif opcao == "4":
            menu_usuario()
        elif opcao == "5":
            print("Cadastro de Vendas")
        elif opcao == "6":
            print("Sair do Sistema")
            break
        else:
            print("Opção invalida< tente novamente")



if __name__ == "__main__":
    conexao = conecta_db()
    while True:
        resultado = login(conexao)
        if resultado is True:
        menu_principal()
    else:
     

  