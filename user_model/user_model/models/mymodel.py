"""Used this resource:
http://stackoverflow.com/questions/33702304/storing-and-validating-encrypted-password-for-login-in-pyramid"""


from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Unicode
)

from passlib.hash import bcrypt

from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(Unicode(255))
    last_name = Column(Unicode(255))
    email = Column(Unicode(255))
    username = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Integer, nullable=False)
    favorite_food = Column(Unicode(255))

    def __init__(
            self,
            first_name,
            last_name,
            email,
            username,
            password,
            favorite_food):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = bcrypt.encrypt(password)
        self.favorite_food = favorite_food

    def validate_password(self, password):
        return bcrypt.verify(password, self.password)
