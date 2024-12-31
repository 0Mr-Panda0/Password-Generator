from flask import Flask, request, render_template
from mylib.password_generator import creating_password
import mysql.connector
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("HOST_NAME"),
    user=os.getenv("USER_NAME"),
    port=os.getenv("PORT"),
    password=os.getenv("PASSWORD"),
    database=os.getenv("DATABASE_NAME"),
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_password", methods=["POST"])
def generate_password():
    length = request.form.get("length")
    special_character = request.form.get("special_character")
    password = creating_password(length, special_character)

    # creating table if not exists
    cursor = db.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS password (id INT AUTO_INCREMENT PRIMARY KEY, password VARCHAR(255))"
    )
    cursor.execute("INSERT INTO password (password) VALUES ('{}')".format(password))
    db.commit()
    # return password
    cursor.execute("SELECT * FROM password ORDER BY id DESC LIMIT 1")
    password = cursor.fetchone()[1]
    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)
