import sys
import os

# Adicionar a raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base
from app.models.user_model import User
from app.models.agenda_model import AgendaItem

if __name__ == "__main__":
    print("📦 Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("✅ Banco de dados pronto TESTE!")
