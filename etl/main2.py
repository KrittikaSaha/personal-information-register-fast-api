from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Table, MetaData, text, insert
from sqlalchemy.orm import sessionmaker

app = FastAPI()

engine = create_engine("sqlite:///personal_info_register.db")
Session = sessionmaker(bind=engine)

#insert
session=Session()
metadata = MetaData()
items = Table("items", metadata)
items = Table("items", metadata, autoload=True, autoload_with=engine)
session.execute(items.insert(), value='item1')


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, session=Session()):
    metadata = MetaData()
    items = Table("items", metadata, autoload=True, autoload_with=engine)
    item = session.query(items).get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, session=Session()):
    metadata = MetaData()
    items = Table("items", metadata, autoload=True, autoload_with=engine)
    item = session.query(items).get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    session.delete(item)
    session.commit()

