# This is John Garcia's Module 7.2 Assignment
# Name: John Garcia
# Date: November 24th 2023
# Assignment: Module 7.2 Assignment
# Purpose: To create a python program that will connect to and query the movies database and output a properly formatted result that matches the assignment requirements.

# Importing the mysql connector
import mysql.connector
from mysql.connector import errorcode

# Creating the config dictionary
config = {
    "user": "root",
    "password": "1234",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True,
}

# Connecting to the database
try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    print("\n\n")

    # This is to create the cursor that will be used to execute the queries
    cursor = db.cursor()

    # This is the creation of the queries that will be used to query the database
    query1 = "SELECT * FROM studio"
    query2 = "SELECT * FROM genre"
    query3 = "SELECT film_name, film_runtime FROM film WHERE film_runtime < 120"
    query4 = "SELECT film_name, film_director FROM film ORDER BY film_director"

    # This is the execution of the first query
    cursor.execute(query1)
    # This is for formatting
    print("-- DISPLAYING Studio RECORDS --")
    # This is the for loop that runs through each record from the query and prints them out
    for (studio_id, studio_name) in cursor:
        # This is for formatting
        print(f'Studio ID: {studio_id} \nStudio Name: {studio_name}')
        print(" ")
    
    # This is the execution of the second query
    cursor.execute(query2)
    # This is for formatting
    print("-- DISPLAYING Genre RECORDS --")
    # This is the for loop that runs through each record from the query and prints them out
    for (genre_id, genre_name) in cursor:
        # This is for formatting
        print(f'Genre ID: {genre_id} \nGenre Name: {genre_name}')
        print(" ")

    # This is the execution of the third query
    cursor.execute(query3)
    # This is for formatting
    print("-- DISPLAYING Short Film RECORDS --")
    # This is the for loop that runs through each record from the query and prints them out
    for (film_name, film_runtime) in cursor:
        # This is for formatting
        print(f'Film Name: {film_name} \nRuntime: {film_runtime}')
        print(" ")

    # This is the execution of the fourth query
    cursor.execute(query4)
    # This is for formatting
    print("-- DISPLAYING Director RECORDS in Order --")
    # This is the for loop that runs through each record from the query and prints them out
    for (film_name, film_director) in cursor:
        # This is for formatting
        print(f'Film Name: {film_name} \nDirector: {film_director}')
        print(" ")

# This is the exception to catch any errors that may occur
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

# This is the finally statement that will close the database connection
finally:
    db.close()

# No sources were used for this assignment
