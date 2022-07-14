from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class UserBase(SQLModel):
    name: str
    phone_number: str


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password: str
    products: List["Product"] = Relationship(back_populates="products")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: int


class UserUpdate(SQLModel):
    id: Optional[int] = None
    name: str
    phone_number: str


class ProductBase(SQLModel):
    name: str = Field(index=True)
    description: str
    price: float
    available = bool
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[User] = Relationship(back_populates="user")


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int


class ProductUpdate(SQLModel):
    id: Optional[int] = None
    name: str
    phone_number: str


class OrderBase(SQLModel):
    quantity: int
    delivery_location: Optional[str]
    delivery_type: str
    description: Optional[str] = "Sem observações"
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    product_id: Optional[int] = Field(default=None, foreign_key="product.id")


class Order(OrderBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[User] = Relationship(back_populates="user")
    product: Optional[Product] = Relationship(back_populates="product")


class OrderCreate(OrderBase):
    pass


class OrderRead(OrderBase):
    id: int


class OrderUpdate(SQLModel):
    id: Optional[int] = None
    name: str
    phone_number: str


##   Schemas   ##


# class ProdutoSimples(SQLModel):
#     id: Optional[int] = None
#     name: str
#     price: float
#     available: bool


# class UsuarioSimples(SQLModel):
#     id: Optional[int] = None
#     name: str
#     phone_number: str


# class LoginData(SQLModel):
#     password: str
#     phone_number: str


# class LoginSuccess(SQLModel):
#     usuario: UsuarioSimples
#     access_token: str


# class Usuario(SQLModel):
#     id: Optional[int] = None
#     name: str
#     phone_number: str
#     password: str
#     produtos: List[ProdutoSimples] = []


# class Produto(SQLModel):
#     id: Optional[int] = None
#     name: str
#     description: str
#     price: float
#     available: bool = False
#     usuario_id: Optional[int]
#     usuario: Optional[UsuarioSimples]


# class Pedido(SQLModel):
#     id: Optional[int] = None
#     quantidade: int
#     local_entrega: Optional[str]
#     tipo_entrega: str
#     description: Optional[str] = "Sem observações"

#     usuario_id: Optional[int]
#     produto_id: Optional[int]

#     usuario: Optional[UsuarioSimples]
#     produto: Optional[ProdutoSimples]
