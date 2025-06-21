from flask import Flask, render_template

app = Flask(__name__)

# Sample data
patients = [
    {"name": "Alice Kim", "visits": 3},
    {"name": "Brian Lee", "visits": 5},
    {"name": "Carlos Rivera", "visits": 2},
    {"name": "Dana Patel", "visits": 4}
]

@app.route("/")
def home():
    names = [p["name"] for p in patients]
    visits = [p["visits"] for p in patients]
    return render_template("dashboard.html", patients=patients, names=names, visits=visits)

if __name__ == "__main__":
    app.run(debug=True)
