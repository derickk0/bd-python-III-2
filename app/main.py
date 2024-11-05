from services.user_services import UserService
from repositories.user_repository import UserRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UserRepository(session)
    service = UserService(repository)

    print("=== SENAI SOLUTION ==="
        "\n1 - Adicionar usuário"
        "\n2 - Pesquisar usuário"
        "\n3 - Atualizar dados de um usuário"
        "\n4 - Excluir usuário"
        "\n5 - Exibir todos os usuários cadastrados"
        "\n0 - Sair")
        
    opcao = input("Digite o número correspondente a opção desejada: ")

    print("\nAdicionando usuário.")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o e-mail do usuário: ")
    senha = input("Digite a senha do usuário: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()