from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_products(db: Session): # SELECT * FROM
    '''
    Função que retorna todos os produtos da tabela "products"
    '''
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int): # SELECT WHERE id = product_id
    '''
    Função que retorna somente um produto, usando "WHERE"
    '''
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate): # INSERT INTO
    # Transformar view para ORM
    db_product = ProductModel(**product.model_dump())

    # Adicionar na tabela
    db.add(db_product)

    # Comitar na tabela
    db.commit()

    # Refresh no banco de dados
    db.refresh(db_product)

    # Retornar pro usuário o item criado
    return db_product

def delete_product(db: Session, product_id: int): # DELETE WHERE id = product_id
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate): # UPDATE WHERE id = product_id
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name
        
    if product.description is not None:
        db_product.description = product.description
        
    if product.price is not None:
        db_product.price = product.price
        
    if product.category is not None:
        db_product.category = product.category
        
    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier

    # Maneira dinâmica
    # for key, value in vars(product).items():
    #     if value is not None:
    #         setattr(db_product, key, value)    

    db.commit()
    db.refresh(db_product)
    return db_product