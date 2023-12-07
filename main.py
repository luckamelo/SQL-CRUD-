from authentication import create_tables, register_user, authenticate
from student_database import StudentDatabase

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.student_database = StudentDatabase()

def main():
    create_tables()  # Adicione esta linha

    users = []  # Lista para armazenar usuários registrados

    while True:
        print("-------CRUD WAGUINHO (LISTA DE ESTUDANTE)--------")
        print("\nEscolha uma opção:")
        print("1. Registrar usuário")
        print("2. Login")
        print("3. Sair")

        choice = input("Digite o número da opção: ")

        if choice == '1':
            # Registra um novo usuário
            new_user = register_user ()
            users.append(new_user) 
            print("Usuário registrado com sucesso!")

        elif choice == '2':
            # Autenticação do usuário
            authenticated_user = authenticate()
            if authenticated_user:
                print("Login bem-sucedido!")

                while True:
                    print("\nEscolha uma opção:")
                    print("1. Adicionar estudante")
                    print("2. Listar estudantes")
                    print("3. Atualizar estudante")
                    print("4. Excluir estudante")
                    print("5. Sair")

                    user_choice = input("Digite o número da opção: ")

                    if user_choice == '1':
                        # Adiciona um novo estudante ao banco de dados
                        student_id = input("Digite o ID do estudante: ")
                        nome = input("Digite o nome do estudante: ")
                        idade = input("Digite a idade do estudante: ")
                        mae = input("Digite o nome da mae: ")
                        pai = input("Digite o nome do pai: ")
                        authenticated_user.student_database.create_student(student_id, nome, idade, mae, pai)
                        print("Estudante adicionado com sucesso!")

                    elif user_choice == '2':
                        # Lista todos os estudantes no banco de dados
                        print("\nLista de Estudantes:")
                        for student in authenticated_user.student_database.students:
                            print(f"ID: {student.student_id}, Nome: {student.nome}, Idade: {student.idade}, Mae: {student.mae}, Pai: {student.pai}")

                    elif user_choice == '3':
                        # Atualiza os detalhes de um estudante existente
                        student_id = input("Digite o ID do estudante que deseja atualizar: ")
                        name = input("Digite o novo nome do estudante: ")
                        age = input("Digite a nova idade do estudante: ")
                        mae = input("Digite o novo nome da mae: ")
                        pai = input("Digite o novo nome do pai: ")
                        if authenticated_user.student_database.update_student(student_id, name, age, mae, pai):
                            print("Estudante atualizado com sucesso!")
                        else:
                            print("Estudante não encontrado.")

                    elif user_choice == '4':
                        # Exclui um estudante do banco de dados
                        student_id = input("Digite o ID do estudante que deseja excluir: ")
                        if authenticated_user.student_database.delete_student(student_id):
                            print("Estudante excluído com sucesso!")
                        else:
                            print("Estudante não encontrado.")
                    
                    elif user_choice == '5':
                        # Sai do programa
                        print("Saindo do programa.")
                        break

                    else:
                        # Mensagem para opção inválida
                        print("Opção inválida. Por favor, escolha uma opção válida.")
            else:
                print("Falha na autenticação. Tente novamente ou registre um novo usuário.")

        elif choice == '3':
            # Sai do programa
            print("Saindo do programa.")
            break

        else:
            # Mensagem para opção inválida
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
