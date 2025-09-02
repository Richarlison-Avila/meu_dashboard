from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import criar_usuario, autenticar_usuario
from pydantic import BaseModel

# Aqui só definimos a tag, SEM prefixo
router = APIRouter(tags=["Autenticação"])

# Schemas
class RegisterSchema(BaseModel):
    nome: str
    email: str
    senha: str

class LoginSchema(BaseModel):
    email: str
    senha: str

@router.post("/register")
def register(payload: RegisterSchema, db: Session = Depends(get_db)):
    usuario = criar_usuario(db, payload.nome, payload.email, payload.senha)
    if not usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}

@router.post("/login")
def login(payload: LoginSchema, db: Session = Depends(get_db)):
    usuario = autenticar_usuario(db, payload.email, payload.senha)
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"id": usuario.id, "nome": usuario.nome, "email": usuario.email}
