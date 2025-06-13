from conexao import conecta_db

def menu_categoria():
    print("----------------------------------------------")
    print("        cadastro de categoria                 ")
    print("----------------------------------------------")
    print("           1 - Listar Categoria                ")
    print("           2 - Consutar  um Categoria por(Id) ")
    print("           3 - Inserir                        ")
    print("           4 - Alterar                        ")
    print("           5 - Deletar                        ")
    print("           6 - Sair                           ")
    print("----------------------------------------------")

    while True:
        opcao = input("Escolha uma opção")

        conexao = conecta_db()

        if opcao == "1":
            listar_categoria(conexao)
        elif opcao == "2":
            consultar_categoria_id(conexao)            
        elif opcao == "3":
            inserir_categoria(conexao)
            listar_categoria(conexao)
        elif opcao == "4":
            listar_categoria(conexao)
            atualizar_categoria(conexao)
            listar_categoria(conexao)
        elif opcao == "5":
            listar_categoria(conexao)
            listar_categoria(conexao)
            deletar_categoria(conexao)
            listar_categoria(conexao)
        elif opcao == "6":
            print("Sair ")
            break
        else:
            print("Opção invalida< tente novamente")

def listar_categoria(conexao):
    cursor = conexao.cursor()
    # Execuçao do select no banco de dados
    cursor.execute("select id,nome from categoria order by id asc")
    #recuperar todos regisros
    registros = cursor.fetchall()
    print("|--------------------------------------|")
    for registro in registros:
        print(f"| ID: {registro[0]} - Nome: {registro[1]}")
        print("|------------------------------------ ---|")

def consultar_categoria_id(conexao):
    id = input("Digite o ID:")
    cursor = conexao.cursor()
    cursor.execute("select id,nome from categoria where id ="+ id)
    registro = cursor.fetchone()

    if registro is None:
        print("Categoria não encontrado:")
    else:
        print(F"| ID:{registro[0]}")
        print(F"| ID:{registro[1]}")


def inserir_categoria(conexao):
    print("Inserindo o Categoria ..:")
    cursor = conexao.cursor()
    nome = input("Nome :")
    sql_insert ="insert into categoria (nome) values ('" + nome +"')"
    cursor.execute( sql_insert)
    conexao.comit()
       
    
def atualizar_categoria(conexao):
    print("Alterando dados dos categoria")
    cursor = conexao.cursor()
    nome = input("Nome :")
    sql_update = "update categoria set nome = '" + nome +"'where id = "+ id
    cursor.execute(sql_update)
    conexao.commit()


def deletar_categoria(conexao):
    print("Alterando dados dos categoria")
    cursor = conexao.cursor()
    id = input("Digite o id :")
    sql_delete = "delete from categoria where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()
    










