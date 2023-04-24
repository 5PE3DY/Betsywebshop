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


class Product(BaseModel):
    name = CharField()
    description = CharField()
    price = FloatField()
    quantity = IntegerField()
    tags = ForeignKeyField(Tag, backref="tags_product")

class UserProduct(BaseModel):
    owner = CharField()
    product = CharField()
    quantity = IntegerField()

class OrderTransaction(BaseModel):
    date = CharField()
    user = CharField()
    product = CharField()
    quantity = IntegerField()