from flask import Flask, request, render_template
from pass_gen.password_generator import creating_password
from pass_gen.database_conn import create_table, insert_password, get_last_password

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate_password", methods=["POST"])
def generate_password():
    length = request.form.get("length")
    special_character = request.form.get("special_character")
    password = creating_password(length, special_character)

    # creating table if not exists
    create_table()

    # insert password into database
    insert_password(password)

    # get last password from database
    password = get_last_password()

    # return the password to the template
    return render_template("index.html", password=password)


if __name__ == "__main__":
    app.run(debug=True)
