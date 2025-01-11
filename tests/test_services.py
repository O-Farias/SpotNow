import pytest
import logging
from app.services import criar_usuario, criar_reserva, listar_reservas

# Configurar o logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_criar_usuario():
    usuario = criar_usuario("Teste User")
    assert usuario.nome == "Teste User", "O nome do usuário não foi salvo corretamente"
    logger.info(f"✅ Teste criar_usuario passou: {usuario.nome}")

def test_criar_reserva():
    usuario = criar_usuario("Reserva User")
    reserva = criar_reserva(usuario.id, "Reserva de Teste")
    assert reserva.descricao == "Reserva de Teste", "A descrição da reserva não foi salva corretamente"
    logger.info(f"✅ Teste criar_reserva passou: {reserva.descricao}")

def test_listar_reservas():
    usuario = criar_usuario("Listagem User")
    criar_reserva(usuario.id, "Primeira Reserva")
    criar_reserva(usuario.id, "Segunda Reserva")

    reservas = listar_reservas()
    assert len(reservas) >= 2, "As reservas não foram listadas corretamente"
    logger.info(f"✅ Teste listar_reservas passou: Total de {len(reservas)} reservas listadas")
