from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

# Modelo de usuário
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)

    # Relacionamento com a tabela Reserva
    reservas = relationship('Reserva', back_populates='usuario')


# Modelo de reserva
class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    data_reserva = Column(DateTime, default=datetime.datetime.utcnow)
    descricao = Column(String, nullable=False)

    # Relacionamento com a tabela Usuario
    usuario = relationship('Usuario', back_populates='reservas')
