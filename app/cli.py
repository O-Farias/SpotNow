import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.services import criar_usuario, criar_reserva, listar_reservas
from colorama import Fore, Style, init


init(autoreset=True)

def menu_principal():
    while True:
        print(f"{Fore.CYAN}=== Sistema de Reservas ===")
        print(f"{Fore.YELLOW}1.{Style.RESET_ALL} Criar Usuário")
        print(f"{Fore.YELLOW}2.{Style.RESET_ALL} Criar Reserva")
        print(f"{Fore.YELLOW}3.{Style.RESET_ALL} Listar Reservas")
        print(f"{Fore.YELLOW}4.{Style.RESET_ALL} Sair")
        
        opcao = input(f"{Fore.GREEN}Escolha uma opção: {Style.RESET_ALL}")

        if opcao == '1':
            nome = input(f"{Fore.BLUE}Digite o nome do usuário: {Style.RESET_ALL}")
            usuario = criar_usuario(nome)
            print(f"{Fore.GREEN}Usuário {usuario.nome} criado com sucesso!{Style.RESET_ALL}")
        elif opcao == '2':
            usuario_id = input(f"{Fore.BLUE}Digite o ID do usuário: {Style.RESET_ALL}")
            descricao = input(f"{Fore.BLUE}Digite a descrição da reserva: {Style.RESET_ALL}")
            reserva = criar_reserva(usuario_id, descricao)
            print(f"{Fore.GREEN}Reserva '{reserva.descricao}' criada com sucesso!{Style.RESET_ALL}")
        elif opcao == '3':
            reservas = listar_reservas()
            if reservas:
                print(f"{Fore.MAGENTA}=== Lista de Reservas ==={Style.RESET_ALL}")
                for reserva in reservas:
                    print(f"{Fore.CYAN}[ID {reserva.id}]{Style.RESET_ALL} {reserva.descricao} - {Fore.YELLOW}Usuário ID: {reserva.usuario_id}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Nenhuma reserva encontrada.{Style.RESET_ALL}")
        elif opcao == '4':
            print(f"{Fore.GREEN}Encerrando o sistema...{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opção inválida! Tente novamente.{Style.RESET_ALL}")

        print()  

if __name__ == "__main__":
    menu_principal()
