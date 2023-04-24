# Betsywebshop
Betsy bike webshop is mainly focust on the batavus brand for now as example


To use this webshop:

1.  Run the file setupdb.py. This will create our database (database.db). Existing or not, the file database.db will be deleted and the application will create a new one based on the setupdb.py data.

if __name__ == "__main__":
    delete_database()
    populate_test_data()
    


    
Initializing database, please wait...
Database Successfully Created!

2.  Go to the file main.py, remove the comments from the functionality you want to perform and run the file.


    SEARCH FUNCTION by TERM 

    search('Batavus Finez E-go')
    search('Batavus Finez E-go Power Exclusive')
    search('Batavus Altura E-go Power')
    search('Batavus Altura E-go Power Pro')
    search('Batavus Dinsdag E-go Classic')
