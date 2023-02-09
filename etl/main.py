#
################################################ Connect FastApi with database ########################################################################
#from fastapi import FastAPI
#from fastapi.responses import JSONResponse
#from pydantic import BaseModel
from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#
##app = FastAPI()
##
### Connect to the database
##engine = create_engine("sqlite:///items.db")
##SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
##
##
from sqlalchemy import create_engine, Column, Integer, String,text, Table, MetaData
##from sqlalchemy.ext.declarative import declarative_base
##
##Base = declarative_base()
### Define the database model
##class Item(Base):
##    __tablename__ = "items"
##    id = Column(Integer, primary_key=True, index=True)
##    name = Column(String, unique=True, index=True)
##
##@app.get("/")
##def read_items():
##    # Get a database session
##    session = SessionLocal()
##    # Query database
##    items = session.query(Item).all()
##    
##    # Convert the results to a list of dictionaries
##    items_list = [{"id": item.id, "name": item.name} for item in items]
##    return items_list
#
#
#
#from fastapi import FastAPI
#from fastapi import HTTPException
#from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy import Column, Integer, String
#
#app = FastAPI()
#Base = declarative_base()
#
#class Item(Base):
#    __tablename__ = "items"
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#
#engine = create_engine("sqlite:///items.db")
#Session = sessionmaker(bind=engine)
#
##@app.get("/items/{item_id}")
##def read_item(item_id: int, skip: int = 0, limit: int = 100):
##    session = Session()
##    item = session.query(Item).filter(Item.id == item_id).first()
##    #if item is None:
##    #    raise HTTPException(status_code=404, detail="Item not found")
##    return item
#
#
#engine = create_engine("sqlite:///items.db")
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#def read_items():
#    # Get a database session
#    session = SessionLocal()
#    # Query database
#    items = session.query(Item).all()
#    
#    # Convert the results to a list of dictionaries
#    items_list = [{"id": item.id, "name": item.name} for item in items]
#    return items_list


from fastapi import FastAPI
from models import get_data, delete_data, get_duplicate_data, update_data

app = FastAPI()


#@app.get("/delete/")
#def read_items():
#    delete_data()
#
#@app.get("/items/{item_id}")
#def read_item(item_id: int, skip: int = 0, limit: int = 100):
#    items= get_data()
#    #item = items.filter(Item.id == item_id).first()
#    #if item is None:
#    #    raise HTTPException(status_code=404, detail="Item not found")
#    return items
#
engine = create_engine('sqlite:///db.sqlite3', pool_size=5, max_overflow=0)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#@app.delete("/items/{item_id}")
#def delete_data(id: int):
#    db = SessionLocal()
#    result = db.execute(text("delete FROM items"))
#    #items = [{"id": row[0], "name": row[1]} for row in result]
#    
#    db.expire_all()
#    db.close()
#    #return items
#    #session.query(items).filter(items.id == id).delete()
#    #session.commit()
#    #session.close()


db = SessionLocal()


#def get_operation():
#    try:
#        db.begin_nested()
#        # perform your database operations here
#
#        db.expire_all()
#        return {"items": get_data()}
#        db.commit()
#    except Exception as e:
#        db.rollback()
#        raise e
#    finally:
#        db.close()
#

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items")
def read_items():
    db.begin_nested()
    # perform your database operations here
 
    db.expire_all()
    items= {"items": get_data()}
    db.commit()
    return items



@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    #db = SessionLocal()
    
    db.begin_nested()
    # perform your database operations here
    # Delete the item from the data store
    #db.delete(item_id)
    #result =  db.execute(text("delete FROM items"))
    db.commit()
    delete_data(id1=item_id)
    #items =  {"items": get_data()}
    db.close()
    return {"message": "Item deleted"}

@app.get("/items/duplicate")
def read_duplicate_items():
    db.begin_nested()
    # perform your database operations here
 
    db.expire_all()
    items= {"items": get_duplicate_data()}
    db.commit()
    return items


@app.put("/items/update")
def update_item_data(item_id: int, item_data: str):
    db.begin_nested()
    # perform your database operations here
 
    db.expire_all()
    update_data(id=item_id, name=item_data)
    db.commit()
    return {"message": "Item updated"}