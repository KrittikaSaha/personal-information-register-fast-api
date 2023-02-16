from sqlalchemy.orm import Session
from fastapi import FastAPI, Header,Depends
from models import get_db, get_data, delete_data, get_duplicate_data, update_data
from credentials import api_key_secret

app = FastAPI(title="Personal Information Register FastAPI Application",
              description="FastAPI Application to store and update user personal data with Swagger and Sqlalchemy",
              version="1.0.0",)


# gets root welcome message
@app.get("/")
def read_root(api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    return {"Hello": "Welcome to the personal register API"}

#get all items in database
@app.get("/items")
def read_items(db: Session = Depends(get_db),api_key: str = Header(None)):
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        # perform your database operations here
    
        db.expire_all()
        items= {"items": get_data(db=db)}
        db.commit()
        return items


#delete items from bd using id
@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db),api_key: str = Header(None)):
    
    if api_key != api_key_secret:
        return {"message": "Invalid API Key"}
    else:
        db.begin_nested()
        db.commit()
        delete_data(id1=item_id, db=db)
        return {"message": "Item deleted"}


#get users with duplicate email ids
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

# update or add items to db
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