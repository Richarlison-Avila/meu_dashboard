from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# --- Configuração do banco ---
SQLALCHEMY_DATABASE_URL = "sqlite:///./projeto_vendas.db"

# Para MySQL futuramente:
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://usuario:senha@localhost/nome_do_banco"

# --- Criando engine ---
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# --- Criando sessão ---
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Base para os models ---
Base = declarative_base()

# --- Função para injetar sessão nas rotas ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
