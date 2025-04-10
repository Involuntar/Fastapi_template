from database import Base
from sqlalchemy import Column, Integer, String, Float


class Planet(Base):
    __tablename__="planets"
    id = Column(Integer, primary_key=True, autoincrement=True)
    planet_name = Column(String(50), unique=True)
    planet_mass = Column(Float)
    planet_diameter = Column(Float)

class Product(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), unique=True)