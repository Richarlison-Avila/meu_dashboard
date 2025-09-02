# app/services/agenda_service.py
from sqlalchemy.orm import Session
from app.models.agenda_model import AgendaItem

def criar_item(db: Session, dados: dict) -> AgendaItem:
    """Cria um novo item de agenda."""
    item = AgendaItem(**dados)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def listar_itens(db: Session) -> list[AgendaItem]:
    """Lista todos os itens da agenda, ordenados por data de início."""
    return db.query(AgendaItem).order_by(AgendaItem.inicio.asc()).all()

def obter_item(db: Session, item_id: int) -> AgendaItem | None:
    """Obtém um item da agenda pelo ID."""
    return db.query(AgendaItem).filter(AgendaItem.id == item_id).first()

def atualizar_item(db: Session, item_id: int, dados: dict) -> AgendaItem | None:
    """Atualiza um item da agenda pelo ID."""
    item = db.query(AgendaItem).filter(AgendaItem.id == item_id).first()
    if not item:
        return None
    for k, v in dados.items():
        setattr(item, k, v)
    db.commit()
    db.refresh(item)
    return item

def deletar_item(db: Session, item_id: int) -> bool:
    """Deleta um item da agenda pelo ID."""
    item = db.query(AgendaItem).filter(AgendaItem.id == item_id).first()
    if not item:
        return False
    db.delete(item)
    db.commit()
    return True
