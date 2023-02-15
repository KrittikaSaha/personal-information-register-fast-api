#from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

##@app.get("/items/{item_id}")
##def read_item(item_id: int, skip: int = 0, limit: int = 100):
##    session = Session()
##    item = session.query(Item).filter(Item.id == item_id).first()
##    #if item is None:
##    #    raise HTTPException(status_code=404, detail="Item not found")
##    return item
#



from fastapi import FastAPI, Header,Depends
from models import get_db, get_data, delete_data, get_duplicate_data, update_data

app = FastAPI()

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
from credentials import api_key_secret

@app.get("/")
def read_root(api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    return {"Hello": "World"}

@app.get("/items")
def read_items(db: Session = Depends(get_db),api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        # perform your database operations here
    
        db.expire_all()
        items= {"items": get_data(db)}
        db.commit()
        return items



@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db),api_key: str = Header(None)):
    
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        # perform your database operations here
        # Delete the item from the data store
        #db.delete(item_id)
        #result =  db.execute(text("delete FROM items"))
        db.commit()
        delete_data(id1=item_id, db=db)
        #items =  {"items": get_data()}
        #db.close()
        return {"message": "Item deleted"}

@app.get("/items/duplicate")
def read_duplicate_items(email_id:str, db: Session = Depends(get_db),api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        # perform your database operations here
    
        db.expire_all()
        items= {f"users having duplicate email_id: {email_id}": get_duplicate_data(email_id, db)}
        db.commit()
        return items


@app.put("/items/update")
def update_item_data(item_id: int, user_first_name: str, 
                     user_last_name: str, user_email: str, 
                     user_gender: str, user_ip_address: str, 
                     user_country_code: str, db: Session = Depends(get_db),api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        # perform your database operations here
    
        db.expire_all()
        update_data(id=item_id, first_name=user_first_name, last_name=user_last_name, 
                    email=user_email, gender=user_gender, ip_address=user_ip_address, country_code=user_country_code,db=db)
        db.commit()
        return {"message": "Item updated"}