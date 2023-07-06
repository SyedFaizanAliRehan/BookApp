from pydantic import BaseModel
from Database.models import BookModel,AuthorModel

class UserValidator(BaseModel):
    id : int
    username : str

class AuthorValidator(BaseModel):
    id : int
    name : str


class BookValidator(BaseModel):
    id : int
    title : str
    author_id: int
