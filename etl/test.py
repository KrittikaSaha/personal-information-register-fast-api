from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Define your database models using SQLAlchemy
# ...

# Connect to the database
engine = create_engine("postgresql://user:password@localhost/database")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define an endpoint that queries the database
@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 100):
    # Get a database session
    db = SessionLocal()

    # Query the database
    items = db.query(Item).offset(skip).limit(limit).all()

    # Return a JSON response
    return JSONResponse(content={"items": items})


############################################### Connect FastApi with database ########################################################################
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Connect to the database
engine = create_engine("sqlite:///items.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Define the database model
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

@app.get("/")
def read_items():
    # Get a database session
    session = SessionLocal()
    # Query database
    items = session.query(Item).all()
    
    # Convert the results to a list of dictionaries
    items_list = [{"id": item.id, "name": item.name} for item in items]
    return items_list

    




############################################### Create database. ########################################################################

from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define a model for the database table
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)

# Connect to the database
engine = create_engine("sqlite:///items.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Insert data into the database using raw SQL statements
session = Session()
session.execute(text("INSERT INTO items (name) VALUES ('item1')"))
session.execute(text("INSERT INTO items (name) VALUES ('item2')"))

session.commit()

##########################################.  sql to check data. #################################################################################

# Execute a raw SQL statement
result = session.execute(text("SELECT * FROM items"))

# Convert the results to a list of dictionaries
items_list = [{"id": row[0], "name": row[1]} for row in result]

print(items_list)
