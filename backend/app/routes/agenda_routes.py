from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine
from app.services.agenda_service import (
    criar_item,
    listar_itens,
    obter_item,
    atualizar_item,
    deletar_item
)
from pydantic import BaseModel
from datetime import datetime

# Criando o router com prefixo e tags já definidos
router = APIRouter(prefix="/agenda", tags=["Agenda"])

# Garantir que a tabela exista
Base.metadata.create_all(bind=engine)

# Schemas Pydantic
class AgendaSchema(BaseModel):
    titulo: str
    descricao: str | None = None
    inicio: datetime
    fim: datetime | None = None
    status: str = "pendente"
    prioridade: str = "normal"

class AgendaUpdateSchema(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    inicio: datetime | None = None
    fim: datetime | None = None
    status: str | None = None
    prioridade: str | None = None

# Rotas
@router.get("/")
def listar(db: Session = Depends(get_db)):
    """Listar todos os itens da agenda"""
    return listar_itens(db)

@router.post("/")
def criar(payload: AgendaSchema, db: Session = Depends(get_db)):
    """Criar um novo item na agenda"""
    return criar_item(db, payload.model_dump())

@router.get("/{item_id}")
def obter(item_id: int, db: Session = Depends(get_db)):
    """Obter um item específico da agenda"""
    item = obter_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.patch("/{item_id}")
def atualizar(item_id: int, payload: AgendaUpdateSchema, db: Session = Depends(get_db)):
    """Atualizar um item existente na agenda"""
    item = atualizar_item(db, item_id, payload.model_dump(exclude_unset=True))
    if not item:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.delete("/{item_id}")
def deletar(item_id: int, db: Session = Depends(get_db)):
    """Deletar um item da agenda"""
    if not deletar_item(db, item_id):
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"ok": True}
