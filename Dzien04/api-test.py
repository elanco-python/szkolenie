
# pip install Flask

from flask import Flask, jsonify, make_response, request
import math

# deklaracja aplikacji Flask
app = Flask("MyApiServer")

# generyczna odpowiedz zwracana przez API
def create_reponse(message, code):
    resp = make_response(message, code)
    resp.mimetype = 'application/json'
    return resp

# deklaracja routingu
@app.route('/')
# funkcja realizująca deklarację routingu
def hello():
    return "Hello world!"

# deklaracja routingu
@app.route('/<name>')
def papuga(name):
    return "Papuguję: "+name

# deklaracja routingu
@app.route('/api/ping', methods=['GET'])
def ping():
    return create_reponse(jsonify({"status" : "OK"}), 200)

# deklaracja routingu
@app.route('/api/isPrime/<number>')
def check_is_prime(number):
    try:
        number = int(number)
        if (number < 2):
            return create_reponse(jsonify({"status" : "OK", "msg" : "Not prime number"}), 409)
        else:
            for i in range(2, int(math.sqrt(number)) + 1):
                if number % i == 0:
                    return create_reponse(jsonify({"status" : "OK", "msg" : "Not prime number"}), 409)
            return create_reponse(jsonify({"status" : "OK"}), 200)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)

# deklaracja routingu
@app.route('/api/form', methods=['POST'])
def check_user():
    try:
        user = request.args["user"]
        password = request.args["pass"]
        if user=="test" and password=="admin":
            return create_reponse(jsonify({"status": "OK"}), 200)
        else:
            return create_reponse(jsonify({"status": "ERROR", "msg": "Not valid password"}), 409)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)


@app.route("/api/saveData", methods=['POST'])
def save_data():
    try:
        data = request.json
        s = data["imie"] + " " + data["nazwisko"]
        return create_reponse(jsonify({"status": "OK", "result" : s}), 200)
    except Exception as exc:
        return create_reponse(jsonify({"status" : "ERROR", "error" : str(exc) }), 500)


@app.after_request
def add_headers(response):
    response.headers["Server"] = "My own API Server"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    response.headers["App-Id"] = "Zajecia z Pythona"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

# uruchom aplikację na localhost, port 1234 w trybie DEBUG
app.run(port=1234, debug=True)