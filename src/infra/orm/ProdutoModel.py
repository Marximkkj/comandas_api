from infra import database
from sqlalchemy import BLOB, DECIMAL, Column, VARCHAR, Integer

# ORM
class ProdutoDB(database.Base):
    __tablename__ = 'tb_produto'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    valor_unitario = Column(DECIMAL(11,2), nullable=False)
    descricao = Column(VARCHAR(200), nullable=False)
    foto = Column(BLOB(bytes), nullable=True)

    def __init__(self, id, nome, valor_unitario, foto, descricao):
        self.id = id
        self.nome = nome
        self.valor_unitario = valor_unitario
        self.descricao = descricao
        self.foto = foto
