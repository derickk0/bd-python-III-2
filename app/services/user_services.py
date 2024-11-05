from models.user_model import User
from repositories.user_repository import UserRepository


class UserService:

    def __init__(self, respository: UserRepository):
        self.repository = respository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = User(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado.")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

    def listar_usuarios(self):
        return self.repository.listar_usuario()