from app.models import Usuario, Reserva
from app.database import get_session

def criar_usuario(nome):
    session = get_session()
    novo_usuario = Usuario(nome=nome)
    session.add(novo_usuario)
    session.commit()
    return novo_usuario

def criar_reserva(usuario_id, descricao):
    session = get_session()
    nova_reserva = Reserva(usuario_id=usuario_id, descricao=descricao)
    session.add(nova_reserva)
    session.commit()
    return nova_reserva

def listar_reservas():
    session = get_session()
    return session.query(Reserva).all()
