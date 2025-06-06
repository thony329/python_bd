from cliente import conecta_db

def menu_cliente():
    print("----------------------------------------------")
    print("        cadastro de Cliente                   ")
    print("----------------------------------------------")
    print("           1 - Listar Clientes                ")
    print("           2 - Consutar  um Cliente por(Id)   ")
    print("           3 - Inserir                        ")
    print("           4 - Alterar                        ")
    print("           5 - Deletar                        ")
    print("           6 - Sair                           ")
    print("----------------------------------------------")

    while True:
        opcao = input("Escolha uma opção")

        conexao = conecta_db()

        if opcao == "1":
            listar_cliente(conexao)
        elif opcao == "2":
            consultar_cliente_por_id(conexao)            
        elif opcao == "3":
            inserir_cliente(conexao)
            listar_cliente(conexao)
        elif opcao == "4":
            listar_cliente(conexao)
            atualizar_cliente(conexao)
            listar_cliente(conexao)
        elif opcao == "5":
            listar_cliente(conexao)
            deletar_cliente(conexao)
            listar_cliente(conexao)
        elif opcao == "6":
            print("Sair ")
            break
        else:
            print("Opção invalida< tente novamente")

def listar_cliente(conexao):
    cursor = conexao.cursor()
    # Execuçao do select no banco de dados
    cursor.execute("select id,nome from cliente order by id asc")
    #recuperar todos regisros
    registros = cursor.fetchall()
    print("|--------------------------------------|")
    for registro in registros:
        print(f"| ID: {registro[0]} - Nome: {registro[1]}")
        print("|---------------------------------------|")

def consultar_cliente_por_id(conexao):
    id = input("Digite o ID:")
    cursor = conexao.cursor()
    cursor.execute("select id,nome from cliente where id ="+ id)
    registro = cursor.fetchone()

    if registro is None:
        print("Cliente não encontrado:")
    else:
        print(F"| ID:{registro[0]}")
        print(F"| ID:{registro[1]}")


def inserir_cliente(conexao):
    print("Inserindo o Cliente ..:")
    cusor = conexao.cursor()
    nome = input("Nome :")
    sql_insert ="insert into cliente (nome) values ('" + nome +"')"
    cursor.execute( sql_insert)
    conexao.comit()
       
    
def atualizar_cliente(conexao):
    print("Alterando dados dos clientes")
    cursor = conexao.cursor()
    nome = input("Nome :")
    sql_update = "update cliente set nome = '" + nome +"'where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()


def deletar_cliente(conexao):
    print("Alterando dados dos clientes")
    cursor = conexao.cursor()
    id = input("Digite o id :")
    sql_delete = "delete from cliente where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()




