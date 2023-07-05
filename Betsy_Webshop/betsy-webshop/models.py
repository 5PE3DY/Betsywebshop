from peewee import *

db = SqliteDatabase("database.db")

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    address = CharField()
    payment = IntegerField()


class Tag(BaseModel):
    tag = CharField(unique = True)

class TagProduct(BaseModel):
    tag = ForeignKeyField(Tag)
    Product = ForeignKeyField(tag)

class Product(BaseModel):
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()

class UserProduct(BaseModel):
    owner = CharField()
    product = CharField()
    quantity = IntegerField()

class OrderTransaction(BaseModel):
    date = CharField()
    user = CharField()
    product = CharField()
    quantity = IntegerField()