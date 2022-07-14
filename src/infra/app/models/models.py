from typing import List, Optional

from fastapi import FastAPI, HTTPException, Depends, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    price: float
    available = bool
