from services.user_services import UserService
from repositories.user_repository import UserRepository
from config.database import Session
import os


def main():
    session = Session()
    repository = UserRepository(session)
    service = UserService(repository)

    print("\nAdicionando usuário.")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
    os.system("cls || clear")
    main()