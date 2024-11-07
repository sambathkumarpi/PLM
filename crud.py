# crud.py
from sqlalchemy.orm import Session
from models import User, Product, Manufacturer, BOM, SalesPurchase
from datetime import date

# CRUD operation for creating a new user
def create_user(db: Session, first_name: str, last_name: str, gender: str, mobile_no: str, email: str, user_type: str):
    db_user = User(first_name=first_name, last_name=last_name, gender=gender, mobile_no=mobile_no, email=email, user_type=user_type)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("user added", first_name)
    return db_user

# CRUD operation for creating a new product
def create_product(db: Session, name: str, quantity: int, unit: str, price: float, expiration_date: date):
    db_product = Product(name=name, quantity=quantity, unit=unit, price=price, expiration_date=expiration_date)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# crud.py
def create_manufacturer(db: Session, batch_number: str, bom: str, manufacturing_date: date):
    manufacturer = Manufacturer(batch_number=batch_number, bom=bom, manufacturing_date=manufacturing_date)
    db.add(manufacturer)
    db.commit()
    db.refresh(manufacturer)
    return manufacturer

def create_sales_purchase(db: Session, transaction_type: str, product_name: str, quantity: int, unit: str, supplier_name: str, price: float, transaction_date: date):
    db_product = db.query(Product).filter(Product.name == product_name).first()
    sales_purchase = SalesPurchase(
        transaction_type=transaction_type,
        product_id=db_product.product_id,
        quantity=quantity,
        unit=unit,
        supplier_name=supplier_name,
        price=price,
        transaction_date=transaction_date
    )
    db.add(sales_purchase)
    db.commit()
    db.refresh(sales_purchase)
    return sales_purchase
