# models.py
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    gender = Column(String)
    mobile_no = Column(String, unique=True)
    email = Column(String, unique=True)
    user_type = Column(String)

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    quantity = Column(Integer)
    unit = Column(String)
    price = Column(Float)
    expiration_date = Column(Date)

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    
    manufacturer_id = Column(Integer, primary_key=True, index=True)
    batch_number = Column(String)
    bom = Column(String)
    manufacturing_date = Column(Date)

class BOM(Base):
    __tablename__ = 'bom'
    
    bom_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    qty = Column(Integer)
    
    product = relationship("Product", back_populates="boms")

class SalesPurchase(Base):
    __tablename__ = 'sales_purchases'
    
    transaction_id = Column(Integer, primary_key=True, index=True)
    transaction_type = Column(String)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)
    unit = Column(String)
    supplier_name = Column(String)
    price = Column(Float)
    transaction_date = Column(Date)
    
    product = relationship("Product", back_populates="sales_purchases")

# Add relationships to the Product model
Product.boms = relationship("BOM", back_populates="product")
Product.sales_purchases = relationship("SalesPurchase", back_populates="product")
