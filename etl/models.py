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

#Insert data into the database using raw SQL statements
#session = SessionLocal()
#session.begin_nested()
#session.execute(text("INSERT INTO items (name) VALUES ('item1')"))
#session.execute(text("INSERT INTO items (name) VALUES ('item2')"))
#session.commit()
def get_data():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM items"))
    items = [{"id": row[0], "name": row[1]} for row in result]
    db.commit()
    db.close()
    return items


def delete_data(id1):
    db = SessionLocal()
    s=text("delete FROM items where id LIKE :item_id" )
    result = db.execute(s,{"item_id":id1})
    db.commit()
    db.close()

def get_duplicate_data():
    db = SessionLocal()
    s=text("select * from items a join ( select name from items group by name having count(*) > 1 ) b on a.name = b.name")

    result = db.execute(s)
    items = [{"id": row[0], "name": row[1]} for row in result]
    db.commit()
    db.close()
    return items

def update_data(id,name):
    db = SessionLocal()
    s = text("INSERT OR REPLACE INTO items (id, name) VALUES (:value1, :value2);")
    result = db.execute(s, {"value1": id, "value2": name})

    db.commit()
    db.close()