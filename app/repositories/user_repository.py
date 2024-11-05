from models.user_model import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def salvar_usuario(self, usuario: User):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisar_usuario_email(self, email: str):
        return self.session.query(User).filter_by(email=email).first()

    def excluir_usuario(self, usuario: User):
        self.session.delete(usuario)
        self.session.commit()
        self.session.refresh(usuario)

    def listar_usuario(self):
        return self.session.query(User).all()