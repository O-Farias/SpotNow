# 🎯 SpotNow - Sistema de Reservas

**SpotNow** é um sistema de reservas desenvolvido em Python, totalmente focado no backend. A aplicação permite criar usuários, realizar reservas e listar todas as reservas cadastradas de maneira simples e intuitiva.

---

## 💡 Funcionalidades

- 📋 **Criar Usuários:** Cadastre usuários com facilidade.
- 📝 **Criar Reservas:** Adicione reservas associadas a usuários existentes.
- 📄 **Listar Reservas:** Visualize todas as reservas realizadas no sistema.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **SQLAlchemy** (ORM)
- **SQLite** (Banco de Dados)
- **Pytest** (Testes automatizados)

---

## 🛠️ Como Configurar e Rodar o Projeto

### Pré-requisitos

- **Python 3.10+** instalado.
- **Virtualenv** para isolar dependências.

### Passos

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/O-Farias/SpotNow.git
   cd SpotNow
   ```

2. **Crie e ative o ambiente virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Para Linux/Mac
   venv\Scripts\activate      # Para Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados**:

   ```bash
   PYTHONPATH=. python app/init_db.py
   ```

5. **Rode o sistema**:

   ```bash
   python app/cli.py
   ```


## 🧪 Testes Automatizados

O projeto conta com testes automatizados utilizando o **pytest**. Para rodar os testes:

```bash
pytest -v -s tests/
```

Você verá um retorno detalhado indicando quais testes passaram. 🚀

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

