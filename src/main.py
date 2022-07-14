from mimetypes import init
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from infra.app.config.database import init_db, get_session


from infra.app.models.models import *

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def start():
    init_db()


@app.post("/products")
def create_product(product: ProductBase):
    return {"Msg": product}


@app.get("/products")
def get_products():
    return {"Msg": "Tá aqui ó"}
