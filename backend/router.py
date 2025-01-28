from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
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

@router.get('/products/', response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    '''
    Rota para ler todos os produtos do banco de dados
    '''
    products = get_products(db)
    return products

@router.get('/products/{product_id}', response_model=ProductResponse)
def read_one_product(product_id: int, db: Session = Depends(get_db)):
    '''
    Rota para ler um dos produtos do banco de dados
    '''
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(
            status_code=404,
            detail='O produto que você deseja acessar não existe.'
            )
    return db_product
    
@router.post('/products/', response_model=ProductResponse)
def post_product(product: ProductCreate, db: Session = Depends(get_db)):
    '''
    Rota para adicionar um item no banco de dados
    '''
    return create_product(db, product)

@router.delete('/products/{product_id}', response_model=ProductResponse)
def delete_product_rt(product_id: int, db: Session = Depends(get_db)):
    '''
    Rota para deletar um item no banco de dados
    '''
    product_db = delete_product(db, product_id)
    if product_db is None:
        raise HTTPException(
            status_code=404,
            detail='O produto que você deseja deletar não existe.'
            )
    return product_db

@router.put('/products/{product_id}', response_model=ProductResponse)
def put_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    '''
    Rota para atualizar um item no banco de dados
    '''
    product_db = update_product(db, product_id, product)
    if product_db is None:
        raise HTTPException(
            status_code=404,
            detail='O produto que você deseja atualizar não existe.'
        )
    return product_db