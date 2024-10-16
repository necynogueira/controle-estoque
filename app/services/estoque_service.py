from sqlalchemy.orm import Session
from app import models


def adicionar_produto(db: Session, produto_id: int, nome: str, preco: float, quantidade: int):
    novo_produto = models.Produto(id=produto_id, nome=nome, preco=preco, quantidade=quantidade)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def remover_produto(db: Session, produto_id: int, quantidade: int):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if produto:
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
            db.commit()
            return produto
        else:
            return {"message": "Quantidade insuficiente"}
    return {"message": "Produto não encontrado"}

def atualizar_estoque(db: Session, produto_id: int, quantidade: int):
    produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if produto:
        produto.quantidade = quantidade
        db.commit()
        return produto
    return {"message": "Produto não encontrado"}

def gerar_relatorio(db: Session):
    produtos = db.query(models.Produto).all()
    return produtos
