from os import stat
from fastapi import FastAPI, status
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


# Product Routes
@app.post("/products", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
def create_product(*, session: Session = Depends(get_session), product: ProductCreate):
    db_product = Product.from_orm(product)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


@app.get("/products", response_model=List[ProductRead], status_code=status.HTTP_200_OK)
def read_products(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    products = session.exec(select(Product).offset(offset).limit(limit)).all()
    return products


# User Routes

# Order Routes
