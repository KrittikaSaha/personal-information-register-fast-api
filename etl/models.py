from sqlalchemy import create_engine, Column, Integer, String,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

SQLALCHEMY_DATABASE_URL = "sqlite:///personal_data.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=0, connect_args={"check_same_thread": False},echo=True)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#session = SessionLocal()
def create_database():
    #Insert data into the database using raw SQL statements
    session = SessionLocal()
    session.begin_nested()
    session.execute(text("INSERT INTO items (name) VALUES ('item1')"))
    session.execute(text("INSERT INTO items (name) VALUES ('item2')"))
    session.commit()
    session.close()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_data(db):
    #db = SessionLocal()
    result = db.execute(text("SELECT * FROM items"))
    items = [{"id": row[0], "name": row[1]} for row in result]
    db.commit()
    #db.close()
    return items


def delete_data(id1, db):
    #db = SessionLocal()
    s=text("delete FROM items where id LIKE :item_id" )
    result = db.execute(s,{"item_id":id1})
    db.commit()
    #db.close()

def get_duplicate_data(item, db):
    #db = SessionLocal()
    #s = text("select * from items a join ( select " + nm + " from items group by " + nm + " having count(*) > 1 ) b on a." + nm + " = b." + nm + "")

    s = text("select * from items a join ( select name from items group by name having count(*) > 1 ) b on a.name = b.name  where a.name = '"+ item +"'")
    result = db.execute(s)
    #s=text("select * from items a join ( select name from items group by name having count(*) > 1 ) b on a.name = b.name")

    #result = db.execute(s,{"name": nm})
    items = [{"id": row[0], "name": row[1]} for row in result]
    db.commit()
    #db.close()
    return items

def update_data(id,name,db):
    #db = SessionLocal()
    s = text("INSERT OR REPLACE INTO items (id, name) VALUES (:value1, :value2);")
    result = db.execute(s, {"value1": id, "value2": name})

    db.commit()
    #db.close()