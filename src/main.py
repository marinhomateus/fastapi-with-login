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


@app.get("/products/{product_id}", response_model=ProductReadWithUser)
def read_product(*, product_id: int, session: Session = Depends(get_session)):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.patch("/products/{product_id}", response_model=ProductRead)
def update_product(
    *,
    session: Session = Depends(get_session),
    product_id: int,
    product: ProductUpdate,
):
    db_product = session.get(Product, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    product_data = product.dict(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


# User Routes
@app.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(*, session: Session = Depends(get_session), user: UserCreate):
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users", response_model=List[UserRead], status_code=status.HTTP_200_OK)
def read_users(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users


@app.get("/users/{user_id}", response_model=UserReadWithProducts)
def read_user(*, user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Order Routes
@app.post("/orders", response_model=OrderRead, status_code=status.HTTP_201_CREATED)
def create_order(*, session: Session = Depends(get_session), order: OrderCreate):
    db_order = Order.from_orm(order)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    return db_order


@app.get("/orders", response_model=List[OrderRead], status_code=status.HTTP_200_OK)
def read_orders(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
):
    orders = session.exec(select(Order).offset(offset).limit(limit)).all()
    return orders
