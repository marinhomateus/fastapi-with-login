from sqlmodel import SQLModel
from typing import Optional, List


class ProdutoSimples(SQLModel):
    id: Optional[int] = None
    name: str
    preco: float
    disponivel: bool


class Usuario(SQLModel):
    id: Optional[int] = None
    name: str
    phone_number: str
    senha: str
    produtos: List[ProdutoSimples] = []


class UsuarioSimples(SQLModel):
    id: Optional[int] = None
    name: str
    phone_number: str


class LoginData(SQLModel):
    senha: str
    phone_number: str


class LoginSuccess(SQLModel):
    usuario: UsuarioSimples
    access_token: str


class Produto(SQLModel):
    id: Optional[int] = None
    name: str
    detalhes: str
    preco: float
    disponivel: bool = False
    usuario_id: Optional[int]
    usuario: Optional[UsuarioSimples]


class Pedido(SQLModel):
    id: Optional[int] = None
    quantidade: int
    local_entrega: Optional[str]
    tipo_entrega: str
    observacao: Optional[str] = "Sem observações"

    usuario_id: Optional[int]
    produto_id: Optional[int]

    usuario: Optional[UsuarioSimples]
    produto: Optional[ProdutoSimples]
