from fastapi import FastAPI,HTTPException,status
from Database.connection import BASE,engine,db_dependency
from Database import validator,models
from sqlalchemy import exists

#Creates a FastAPI Application
app = FastAPI()

# Creates db and tables.
BASE.metadata.create_all(bind = engine)

@app.get("/",tags=["root"])
async def root():
    return {"message": "Hello World"}

@app.post('/users/',status_code= status.HTTP_201_CREATED)
async def create_user(user:validator.UserValidator,db:db_dependency):
    db_user = models.UserModel(**user.dict())
    db.add(db_user)
    db.commit()

@app.get('/users/',status_code= status.HTTP_201_CREATED)
async def get_user_by_id(user_id:int, db: db_dependency):
    user = db.query(models.UserModel).filter(models.UserModel.id == user_id).first()
    if user is None:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@app.post('/author/',status_code= status.HTTP_201_CREATED)
async def create_author(author:validator.AuthorValidator,db:db_dependency):
    new_author = models.AuthorModel(**author.dict())
    db.add(new_author)
    db.commit()

@app.post('/books/',status_code= status.HTTP_201_CREATED)
async def create_book(book:validator.BookValidator,db:db_dependency):
    new_book = models.BookModel(**book.dict())
    if db.query(exists().where(models.AuthorModel.id == new_book.author_id)).scalar():
        db.add(new_book)
        db.commit()
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Author not found!!!")
    
    