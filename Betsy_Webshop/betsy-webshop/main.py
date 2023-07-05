__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import *
from datetime import datetime

def search(term):
    term = term.lower()
    search_query = Product.select().where(Product.name.contains(term) | Product.description.contains(term))
    if search_query:
        print(f"\nProducts found based on the term: '{term}'")
        for product in search_query:
            print(f"- {product.name}")
    else:
        print(f"\nNo products matching: '{term}' ")



def list_user_products(user_id):
    user_product_list_query = UserProduct.select().where(UserProduct.owner == user_id)
    if user_product_list_query:
        print(f"{user_id}'s products: ")
        for product in user_product_list_query:
            print(f"- {product.product}")
    else:
        print(f"User {user_id} has no products! ")



def list_products_per_tag(tag_id):
    products_list_per_tag_query = TagProduct.select().where(tag_id == tag_id)
    if products_list_per_tag_query:
        print(f"\nProducts found by tag: '{tag_id}' ")
        for product in products_list_per_tag_query:
            print(f"- {product.name}")
    else: 
        print(f"\nThe tag '{tag_id}' has no results.")



def add_product_to_user(user_id, product):
    get_product_query = Product.select().where(Product.name == product)
    get_user_query = User.select().where(User.name == user_id)

    if get_product_query and get_user_query:
        new_product = UserProduct.create(
            owner = user_id,
            product = product,
            quantity = 1,
        )
        print(f"{product} has been added to user {user_id}.")
        return new_product
    else:
        print("User or product not found!")



def remove_product_from_user(product_id):
    try:
        product = UserProduct.get(UserProduct.product == product_id)
        print(f"{product_id} has been removed.")
        return product.delete_instance()
    except DoesNotExist:
        print("No products found!")



def update_stock(product_id, new_quantity):
    update_product_stock = Product.get(Product.name == product_id)
    if update_product_stock:
        print(f"Product:\t    {update_product_stock.name}")
        print(f"Previous Stock:\t{update_product_stock.quantity}")
        update_product_stock.quantity = new_quantity
        update_product_stock.save()
        print(f"New stock:\t    {update_product_stock.quantity}")
    else:
        print("No products found.")



def purchase_product_between_users(product_id, buyer_id, quantity):
    user_of_purchase = User.get(User.name == buyer_id)
    product_of_purchase = Product.get(Product.name == product_id)

    if user_of_purchase and product_of_purchase:
        current_date = datetime.now().date()
        get_date = datetime.strftime(current_date, "%d-%m-%Y")
        quantity_stock_check = product_of_purchase.quantity - quantity
        if quantity_stock_check >= 0:
            order = OrderTransaction.create(
                date = get_date,
                user = buyer_id,
                product = product_id,
                quantity = quantity
            )
            print("-=-" * 20)
            print("ORDER TRANSACTION: ")
            print(f"DATE:\t\t{order.date}\nCLIENT:\t\t{order.user}\nPRODUCT:\t{order.product}\nAMOUNT:\t\t{order.quantity}")

            print("\n")
            add_product_to_user(buyer_id, product_id)
            print("\n")
            list_user_products(buyer_id)

            if quantity_stock_check == 0:
                return remove_product_from_user(product_id)
            print("\nSTOCK UPDATE:")
            return update_stock(product_id, quantity_stock_check)
        else:
            print("Not enough stock.")
    else:
        print("User or products not found.")


def main():
    db.connect()

###### SEARCH FUNCTION by TERM ######

    search('Batavus Finez E-go')
    search('Batavus Finez E-go Power Exclusive')
    search('Batavus Altura E-go Power')
    search('Batavus Altura E-go Power Pro')
    search('Batavus Dinsdag E-go Classic')


###### LIST OF PRODUCTS PER USER ######

    # list_user_products('Henk')
    # list_user_products('Bennie')
    # list_user_products('Laura')

    
###### LIST OF PRODUCTS PER TAG ######

    # list_products_per_tag('bassic')
    # list_products_per_tag('exlusive')
    # list_products_per_tag('power')
    # list_products_per_tag('powerpro')


 ###### ADD A PRODUCT TO A USER ######

    # list_user_products('Sandra')
    # add_product_to_user('Sandra', 'Batavus Altura E-go Power')
    # list_user_products('Sandra')


 ###### REMOVE A PRODUCT FROM  A USER ######

    # list_user_products('Sandra')
    # remove_product_from_user('Batavus Altura E-go Power')
    # list_user_products('Sandra')


###### UPDATE THE STOCK MANUALLY ######

    # update_stock('Batavus Altura E-go Power', 11)


###### PURCHASE PRODUCTS BETWEEN USERS ######

    # purchase_product_between_users('Batavus Finez E-go', 'Henk', 1)
    # purchase_product_between_users('Batavus Dinsdag E-go Classic', 'Laura', 1)
    # list_user_products('Henk')
    # list_user_products('Laura')


    db.close()

if __name__ == "__main__":
    main()