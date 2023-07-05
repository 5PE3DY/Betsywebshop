from models import (db, User, Tag, Product, OrderTransaction, UserProduct)
import os
from time import sleep


def delete_database():
    cwd = os.getcwd()
    database_path = os.path.join(cwd, "database.db")
    if os.path.exists(database_path):
        os.remove(database_path)


def populate_test_data():
    db.connect()
    print("Initializing database, please wait...")
    db.create_tables([User, Tag, Product, UserProduct, OrderTransaction])

    users = [
        {'name': 'Henk Janssens',
        'address': 'Belgie',
        'payment': 1234},
        {'name': 'Bennie Jacobsen',
        'address': 'Amsterdam',
        'payment': 2345},
        {'name': 'Sandra dweiltje',
        'address': 'Zwijndrecht',
        'payment': 3456},
        {'name': 'Laura van Hamelen',
        'address': 'Pannerden',
        'payment': 4567},
    ]

    for user in users:
        User.create(
            name = user['name'],
            address = user['address'],
            payment = user['payment']
        )
    
    tags = ['Basic', 'Exclusive', 'Power', 'Powerpro', ' Pleasure']

    for tag in tags:
        Tag.create(tag = tag)

    products = [
        {'name': 'Batavus Finez E-go',
        'description': 'The ideal comfort bike with a particularly attractive price.',
        'price': 1999.00,
        'quantity': 5,
        'tags': 'basic'},

        {'name': 'Batavus Finez E-go Power Exclusive',
        'description': 'The ultimate comfort bike with maintenance-free belt drive',
        'price': 3699,
        'quantity': 3,
        'tags': 'exclusive'},

        {'name': 'Batavus Altura E-go Power',
        'description': 'A wonderfully comfortable bike with a fully integrated battery for an attractive price. The Altura combines the looks of a city bike with the convenience of an e-bike.',
        'price': 2799,
        'quantity': 10,
        'tags': 'power'},

        {'name': 'Batavus Altura E-go Power Pro',
        'description': 'Enjoy every kilometer even more',
        'price': 3149,
        'quantity': 8,
        'tags': 'powerpro'},

        {'name': 'Batavus Dinsdag E-go Classic',
        'description': 'A trendy electric bike for miles of driving pleasure.',
        'price': 3149,
        'quantity': 15,
        'tags': 'pleasure'},


    ]

    for product in products:
        Product.create(
            name = product['name'],
            description = product['description'],
            price = product['price'],
            quantity = product['quantity'],
    )
    
    # User Products
    user_products = [
        {'owner': 'Henk',
        'product': 'Batavus Finez E-go',
        'quantity': 1,
        },
        {'owner': 'Laura',
        'product': 'Batavus Dinsdag E-go Classic',
        'quantity': 1,
        },
        {'owner': 'Sandra',
        'product': 'Batavus Altura E-go Power',
        'quantity': 2,
        }

    ]

    for user_product in user_products:
        UserProduct.create(
            owner = user_product['owner'],
            product = user_product['product'],
            quantity = user_product['quantity'],
        )
    

    db.close()
    sleep(5)
    print("Database Successfully Created!")

if __name__ == "__main__":
    delete_database()
    populate_test_data()