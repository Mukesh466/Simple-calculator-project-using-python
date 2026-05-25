from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Safe math functions
def safe_eval(expr):
    expr = expr.replace("^", "**")

    allowed = {
        "sin": lambda x: math.sin(math.radians(x)),
        "cos": lambda x: math.cos(math.radians(x)),
        "tan": lambda x: math.tan(math.radians(x)),
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "pi": math.pi,
        "e": math.e,
        "pow": pow
    }

    try:
        result = eval(expr, {"__builtins__": None}, allowed)
        return result
    except:
        return "Error"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expression = data.get("expression", "")

    result = safe_eval(expression)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
