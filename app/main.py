from fastapi import FastAPI
from app.database import engine
from app import models
from app.routes import estoque


app = FastAPI()

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Registrando os endpoints
app.include_router(estoque.router, prefix="/estoque", tags=["Gerenciamento de Estoque"])

@app.get("/")
def root():
    return {"message": "Sistema de Gerenciamento de Estoque"}
