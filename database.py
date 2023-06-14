import mysql.connector
import time

# Wait for MySQL container to start up
time.sleep(60)  # Adjust the delay as needed
# Database connection configuration
db_config = {
    "host": "movie-db",
    "port": 3306,
    "user": "db",
    "password": "123",
    "database": "lalala",
}

# Establish a database connection
db_connection = mysql.connector.connect(**db_config)
db_cursor = db_connection.cursor()

def search_movies_by_year(year_of_release):
    query = "SELECT * FROM hahaha WHERE year_of_release = %s"
    db_cursor.execute(query, (year_of_release,))
    results = db_cursor.fetchall()
    return results

def upload_movie_data(movie_name, year_of_release, box_office, director, producer, cast):
    query = "INSERT INTO hahaha (movie_name, year_of_release, box_office, director, producer, cast) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (movie_name, year_of_release, box_office, director, producer, cast)
    db_cursor.execute(query, values)
    db_connection.commit()
