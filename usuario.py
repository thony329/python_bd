from conexao import conecta_db

def menu_usuario():
    print("----------------------------------------------")
    print("        cadastro de usuario                   ")
    print("----------------------------------------------")
    print("           1 - Listar Usuario                 ")
    print("           2 - Consutar  um usuario por(Id)   ")
    print("           3 - Inserir                        ")
    print("           4 - Alterar                        ")
    print("           5 - Deletar                        ")
    print("           6 - Sair                           ")
    print("----------------------------------------------")

    while True:
        opcao = input("Escolha uma opção")

        conexao = conecta_db()

        if opcao == "1":
            listar_usuario(conexao)
        elif opcao == "2":
            consultar_usuario_por_id(conexao)            
        elif opcao == "3":
            inserir_usuario(conexao)
            listar_usuario(conexao)
        elif opcao == "4":
            listar_usuario(conexao)
            atualizar_produto(conexao)
            listar_usuario(conexao)
        elif opcao == "5":
            listar_usuario(conexao)
            deletar_usuario(conexao)
            listar_usuario(conexao)
        elif opcao == "6":
            print("Sair ")
            break
        else:
            print("Opção invalida< tente novamente")
        
def login (conexao) ->  bool:
    login = input("Digite o Login")
    senha = input("Digite a senha")


    cursor = conexao.cursor()
    sql_listar = """ select id,login,admin from usuario             
                where login = %s and senha  = %s
            """

    # Execuçao do select no banco de dados
    cursor.execute("select id,login,admin from usuario produto order by id asc")
    #recuperar todos regisros
    registros = cursor.fetchall()
    print("|--------------------------------------|")
    for registro in registros:
        print(f"| ID: {registro[0]} - Login: {registro[1]} - admin: {registro[2]} ")
        print("|------------------------------------ ---|")

def consultar_usuario_por_id(conexao):
    id = input("Digite o ID:")
    cursor = conexao.cursor()
    cursor.execute("select id,login,admin from usuario where id ="+ id)
    registro = cursor.fetchone()

    if registro is None:
        print("Usuario não encontrado:")
    else:
        print(f"| ID          ..:{registro[0]}")
        print(f"| Login         :{registro[1]}")      
        print(f"| Admin         :{registro[2]}")

def inserir_usuario(conexao):
    print("Inserindo o Usuário ..:")
    cursor = conexao.cursor()

    login = input("Login :")
    senha = input("Senha :")
    admin = input("Admin :")
    
    sql_insert ="insert into usuario (login,senha,admin) values ( %s,%s,%s )"
    dados =(login,senha,admin)
    cursor.execute( sql_insert, dados)
    conexao.commit()
       
    
def atualizar_usuario(conexao):
    print("Alterando dados dos Usuário")
    cursor = conexao.cursor()
    
    id    = input("ID :")
    login = input("Login :")
    senha = input("Senha :")
    admin = input("Admin :")

    sql_update = "update usuario set login= %s, senha = %s,admin = %s where id = %s"
    dados =(login,senha,admin,id)   
    cursor.execute(sql_update,dados)
    conexao.commit()


def deletar_usuario(conexao):
    print("Alterando dados dos produto")
    cursor = conexao.cursor()
    id = input("Digite o id :")
    sql_delete = "delete from produto where id = "+ id
    cursor.execute(sql_delete)
    conexao.commit()










