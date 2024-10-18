from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obter as variáveis de ambiente
DB_USER = os.getenv("DB_USER", "mysql")  # Valor padrão
DB_PASSWORD = os.getenv("DB_PASSWORD", "mysql")  # Valor padrão
DB_HOST = os.getenv("DB_HOST", "controle-estoque_devcontainer-mysql-db-1")  # Valor padrão
DB_PORT = os.getenv("DB_PORT", "3306")  # Valor padrão
DB_NAME = os.getenv("DB_NAME", "controle_estoque")  # Valor padrão

# Configuração de conexão com o banco de dados MySQL
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Criação do engine
engine = create_engine(DATABASE_URL)

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base de dados declarativa
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()