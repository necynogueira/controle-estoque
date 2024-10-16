from sqlalchemy import Column, Integer, String, Float
from app.database import Base


# Modelo de Produto
class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), index=True)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, nullable=False)
