import psycopg2
from flask import Flask, render_template, request

app = Flask(__name__)
connect = psycopg2.connect("dbname=tutorial user=postgres password=postgres@m")
cur = connect.cursor()  # create cursor


@app.route('/')
def main():
    return render_template("main.html", x='Hello', y=123)


@app.route('/return', methods=['post'])
def re_turn():
    return render_template("main.html")


@app.route('/bye')
def bye():
    return "I love you Sam, you gonna do well"


@app.route('/print_table', methods=['post'])
def print_table():
    cur.execute("SELECT * FROM users;")
    result = cur.fetchall()

    return render_template("print_table.html", users=result)


@app.route('/register', methods=['post'])
def register():
    id = request.form["id"]
    password = request.form["password"]
    send = request.form["send"]

    cur.execute("INSERT INTO users VALUES('{}', '{}');".format(id, password))

    connect.commit()

    return id + " " + password + " " + send


if __name__ == '__main__':
    app.run()
