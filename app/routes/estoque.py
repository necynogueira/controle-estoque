from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.estoque_service import adicionar_produto, remover_produto, atualizar_estoque, gerar_relatorio
from app.database import get_db


router = APIRouter()

@router.post("/adicionar")
def adicionar(produto_id: int, nome: str, preco: float, quantidade: int, db: Session = Depends(get_db)):
    return adicionar_produto(db, produto_id, nome, preco, quantidade)

@router.post("/remover")
def remover(produto_id: int, quantidade: int, db: Session = Depends(get_db)):
    return remover_produto(db, produto_id, quantidade)

@router.put("/atualizar")
def atualizar(produto_id: int, quantidade: int, db: Session = Depends(get_db)):
    return atualizar_estoque(db, produto_id, quantidade)

@router.get("/relatorio")
def relatorio(db: Session = Depends(get_db)):
    return gerar_relatorio(db)
