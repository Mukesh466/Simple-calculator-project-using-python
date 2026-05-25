from flask import Flask, request, jsonify, send_from_directory
import math
import os

app = Flask(__name__, static_folder="../frontend")

# -----------------------------
# SAFE MATH ENGINE
# -----------------------------
def safe_eval(expr):
    try:
        expr = expr.replace("^", "**")

        allowed = {
            # math functions
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pow": pow,

            # constants
            "pi": math.pi,
            "e": math.e,
            "abs": abs
        }

        # evaluate safely
        result = eval(expr, {"__builtins__": None}, allowed)
        return result

    except ZeroDivisionError:
        return "Error: Division by zero"

    except Exception:
        return "Error: Invalid expression"


# -----------------------------
# ROUTES (FRONTEND)
# -----------------------------
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)


# -----------------------------
# API ROUTE (CALCULATOR)
# -----------------------------
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    expression = data.get("expression", "")

    result = safe_eval(expression)
    return jsonify({"result": result})


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
