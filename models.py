from database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Planet(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    planet_name = Column(String(50), unique=True)
    planet_mass = Column(Float)
    planet_diameter = Column(Float)

class Category(Base): #1
    __tablename__="categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(255), unique=True)

class Product(Base): #N
    __tablename__="products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), unique=True)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", backref="products")