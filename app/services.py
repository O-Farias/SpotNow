from app.models import Usuario, Reserva
from app.database import get_session

def criar_usuario(nome):
    """
    Cria um novo usuário no banco de dados e reanexa a instância à sessão.
    """
    session = get_session()
    usuario = Usuario(nome=nome)
    session.add(usuario)
    session.commit()
    session.refresh(usuario)  
    return usuario

def criar_reserva(usuario_id, descricao):
    """
    Cria uma nova reserva associada a um usuário.
    """
    session = get_session()
    nova_reserva = Reserva(usuario_id=usuario_id, descricao=descricao)
    session.add(nova_reserva)
    session.commit()
    session.refresh(nova_reserva)  
    return nova_reserva

def listar_reservas():
    """
    Lista todas as reservas no banco de dados.
    """
    session = get_session()
    return session.query(Reserva).all()
