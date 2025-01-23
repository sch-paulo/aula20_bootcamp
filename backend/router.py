from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product, 
    get_products,
    get_product,
    delete_product,
    update_product
)

router = APIRouter()

@router.get('/products/', response_model=List[ProductResponse]) # rota de buscar todos os itens
def read_all_products(db: Session = Depends(get_db)):
