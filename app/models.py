from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

class Reserva(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    data_reserva = Column(DateTime, default=datetime.datetime.utcnow)
    descricao = Column(String, nullable=False)

    usuario = relationship('Usuario', back_populates='reservas')

Usuario.reservas = relationship('Reserva', order_by=Reserva.id, back_populates='usuario')
