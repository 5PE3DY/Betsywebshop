# Betsywebshop

Betsy bike webshop is mainly focust on the batavus brand for now as example
<br>
<br>
To use this webshop:<br>
1. Run the file setupdb.py. This will create a new database file and delete the existing file.<br>
<br>
	    
    if __name__ == "__main__":
	delete_database()
	populate_test_data() 

	Initializing database, please wait...
	Database Successfully Created!
	
2.	Go to the file main.py, remove the comments from the functionality you want to perform and run the file.

eg.	**SEARCH FUNCTION by TERM**
	
	search('Batavus Finez E-go')<br>
	search('Batavus Finez E-go Power Exclusive')<br>
	search('Batavus Altura E-go Power')<br>
	search('Batavus Altura E-go Power Pro')search('Batavus Dinsdag E-go Classic')<br>
