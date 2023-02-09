import json
# Data to be written
dictionary = {
    "id": "001",
    "first_name": "Anne",
    "last_name": "Kokkoniemi",
    "email": "annek@gmail.com",
    "gender": "0447671303",
    "ip_address": "",
    "country_code": "FI"
}
 
# Serializing json
#json_object = json.dumps(dictionary, indent=4)

from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

engine = create_engine("sqlite:///db.sqlite3")
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Insert data into the database using raw SQL statements
session = SessionLocal()
session.execute(text("INSERT INTO items (name) VALUES ('item1')"))
session.execute(text("INSERT INTO items (name) VALUES ('item2')"))

session.commit()
def get_data():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM items"))
    items = [{"id": row[0], "name": row[1]} for row in result]
    db.close()
    return items

get_data()