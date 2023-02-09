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
session = SessionLocal()
session.begin_nested()
#session.execute(text("INSERT INTO items (name) VALUES ('item1')"))
session.execute(text("INSERT INTO items (name) VALUES ('item2')"))
session.commit()