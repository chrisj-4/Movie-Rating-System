from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect("movieratings.db")
    cursor = conn.cursor()

    if request.method == "POST":
        name = request.form["username"]
        movie = request.form["movie"]
        rating = request.form["rating"]
        review = request.form["review"]

        cursor.execute("INSERT INTO MovieRatings (UserName, MovieTitle, Rating, ReviewText) VALUES (?, ?, ?, ?)",
                       (name, movie, rating, review))
        conn.commit()

    cursor.execute("SELECT * FROM MovieRatings")
    data = cursor.fetchall()
    conn.close()
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
