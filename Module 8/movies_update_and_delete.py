# This is John Garcia's Module 8.2 Assignment
# Name: John Garcia
# Date: November 26th 2023
# Assignment: Module 8.2 Assignment
# Purpose: To create a program that will connect to a database and show desired information before and after an insertion, update, and delete query is executed.

# Importing the mysql connector
import mysql.connector
from mysql.connector import errorcode

# This is the function that will be called to show the desired information when given the proper arguments of cursor and label.
def show_films(cursor, label):
    # This is the query that will be used to show the films.
    query = "SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_id INNER JOIN studio ON film.studio_id = studio.studio_id ORDER BY film_id"
    cursor.execute(query)
    # This is the results that will be fetched from the query.
    results = cursor.fetchall()
    #This is to print the label that is passed from the main function when the show_films function is called.
    print(f'-- {label} --')
    # This is the for loop that will ierate through the results variable and print each result in the desired format.
    for film in results:
        print(f'Film Name: {film[0]}\nDirector: {film[1]}\nGenre Name: {film[2]}\nStudio Name: {film[3]}')
        print(" ")
    print(" ")

# This is the main function that will be called to run the program. I decided to use this so that I can wrap the script, which I find easier to read personally.    
def main():
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
        # This is the cursor that will be used to execute the queries
        cursor = db.cursor()
        # This is the first time the show_films function is called which will show the films before any changes are made.
        show_films(cursor, "DISPLAYING FILMS")
        # This is the insertion query that will be used to insert a 'First Man' into the database.
        insertion_query = "INSERT INTO film (film_name, film_releaseDate, film_runtime,  film_director,studio_id, genre_id ) VALUES ('First Man', '2018', '141', 'Damien Chazelle', '3', '2')"
        # This is the execution of the insertion query
        cursor.execute(insertion_query)
        db.commit()
        # This is the second time the show_films function is called which will show the films after the insertion query has been executed.
        show_films(cursor, "DISPLAYING FILMS AFTER INSERT")
        # This is the update query that will be used to update the genre_id of 'Alien' to be '1' which is the genre_id for Horror.
        update_query = "UPDATE film SET genre_id = '1' WHERE film_id = '2'"
        # This is the execution of the update query
        cursor.execute(update_query)
        db.commit()
        # This is the third time the show_films function is called which will show the films after the update query has been executed.
        show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")
        # This is the delete query that will be used to delete the film with the film_id of '1' which is 'Gladiator'.
        delete_query = "DELETE FROM film WHERE film_id = '1'"
        # This is the execution of the delete query
        cursor.execute(delete_query)
        db.commit()
        # This is the last time the show_films function is called which will show the films after the delete query has been executed.
        show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

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

# This is the call to the main function that will run the program.
main()
# No sources were used for this assignment