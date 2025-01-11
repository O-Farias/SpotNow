import sys
from app.services import criar_usuario, criar_reserva, listar_reservas

def menu_principal():
    while True:
        print("\n=== Sistema de Reservas ===")
        print("1. Criar Usuário")
        print("2. Criar Reserva")
        print("3. Listar Reservas")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do usuário: ")
            usuario = criar_usuario(nome)
            print(f"Usuário {usuario.nome} criado com sucesso!")

        elif escolha == "2":
            usuario_id = int(input("ID do usuário: "))
            descricao = input("Descrição da reserva: ")
            reserva = criar_reserva(usuario_id, descricao)
            print(f"Reserva criada: {reserva.descricao}")

        elif escolha == "3":
            reservas = listar_reservas()
            for r in reservas:
                print(f"[ID {r.id}] {r.descricao} - Usuário ID: {r.usuario_id}")

        elif escolha == "4":
            print("Saindo...")
            sys.exit()

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()
