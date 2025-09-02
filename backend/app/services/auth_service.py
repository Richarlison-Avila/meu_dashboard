# app/services/auth_service.py
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.models.user_model import User

# Contexto para hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return pwd_context.verify(senha, hash_salvo)

def criar_usuario(db: Session, nome: str, email: str, senha: str) -> User | None:
    """Cria um novo usuário no banco (retorna None se o email já existir)."""
    novo = User(nome=nome, email=email, senha=hash_senha(senha))
    db.add(novo)
    try:
        db.commit()
        db.refresh(novo)
        return novo
    except IntegrityError:
        db.rollback()
        return None

def autenticar_usuario(db: Session, email: str, senha: str) -> User | None:
    """Autentica o usuário verificando email e senha."""
    usuario = db.query(User).filter(User.email == email).first()
    if not usuario:
        return None
    if not verificar_senha(senha, usuario.senha):
        return None
    return usuario
