from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import mysql.connector
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Database connection configuration
db_config = {
    "host": "db",
    "port": 3306,
    "user": "root",
    "password": "123",
    "database": "lalala",
}

# Establish a database connection
db_connection = mysql.connector.connect(**db_config)
db_cursor = db_connection.cursor()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/")
def search_movies(request: Request, year_of_release: int = Form(...)):
    query = "SELECT * FROM hahaha WHERE year_of_release = %s"
    db_cursor.execute(query, (year_of_release,))
    results = db_cursor.fetchall()
    return templates.TemplateResponse("index.html", {"request": request, "results": results})

@app.get("/upload_data")
def upload_data(request: Request):
    return templates.TemplateResponse("upload_data.html", {"request": request})

@app.post("/upload_data")
def upload_movie_data(
    request: Request,
    movie_name: str = Form(...),
    year_of_release: int = Form(...),
    box_office: float = Form(...),
    director: str = Form(...),
    producer: str = Form(...),
    cast: str = Form(...)
):
    query = "INSERT INTO hahaha (movie_name, year_of_release, box_office, director, producer, cast) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (movie_name, year_of_release, box_office, director, producer, cast)
    db_cursor.execute(query, values)
    db_connection.commit()
    return templates.TemplateResponse("upload_data.html", {"request": request})

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)