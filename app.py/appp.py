from flask import Flask, request, jsonify, send_from_directory
import math
import os

app = Flask(__name__, static_folder="frontend")

def safe_eval(expr):
    try:
        expr = expr.replace("^", "**")

        allowed = {
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pow": pow,
            "pi": math.pi,
            "e": math.e
        }

        return eval(expr, {"__builtins__": None}, allowed)

    except:
        return "Error"


@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expr = data.get("expression", "")
    result = safe_eval(expr)
    return jsonify({"result": result})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
