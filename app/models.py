from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///personal_data.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=5, max_overflow=0, connect_args={"check_same_thread": False},echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_data(db):
    result = db.execute(text("SELECT * FROM users"))
    items = [{"id": row[0], "first_name": row[1], "last_name": row[2],
              "email": row[3],"gender": row[4],
              "ip_address": row[5],"country_code": row[6]} for row in result]
    db.commit()
    return items


def delete_data(id1, db):
    s=text("delete FROM users where id LIKE :id" )
    db.execute(s,{"id":id1})
    db.commit()

def get_duplicate_data(email_id, db):
    #s = text("select * from items a join ( select " + nm + " from items group by " + nm + " having count(*) > 1 ) b on a." + nm + " = b." + nm + "")

    s = text("select * from users a join ( select email from users group by email having count(*) > 1 ) b on a.email = b.email  where a.email = '"+ email_id +"'")
    result = db.execute(s)
    items = [{"id": row[0], "first_name": row[1], "last_name": row[2]} for row in result]
    db.commit()
    return items

def update_data(id,first_name, last_name, email, gender, ip_address, country_code,db):
    s = text("INSERT OR REPLACE INTO users (id, first_name, last_name, email, gender, ip_address, country_code) VALUES (:value1, :value2, :value3, :value4, :value5, :value6, :value7);")
    db.execute(s, {"value1": id, "value2": first_name,
                   "value3": last_name, "value4": email, "value5": gender, "value6": ip_address, "value7": country_code
                   })
    db.commit()