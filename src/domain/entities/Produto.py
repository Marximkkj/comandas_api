#Marcos Vinicius Arruda Vandresen
from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    preco: float
    descricao: str
    foto: bytes