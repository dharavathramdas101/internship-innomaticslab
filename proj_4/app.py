from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def upper():
    name = request.args.get("name","")
    return f"Hi {name.upper()}" if name else "please give name in query parameter"

@app.route("/random")
def random_number():
    return str(random.randint(1,111))


if __name__ == "__main__":
    app.run(debug=True)