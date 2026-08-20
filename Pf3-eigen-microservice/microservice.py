from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "service": "calculator-microservice"}), 200

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    a = request.args.get('a')
    b = request.args.get('b')

    if not operation or a is None or b is None:
        return jsonify({"error": "Geef 'operation', 'a' en 'b' mee als parameters"}), 400

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify({"error": "'a' en 'b' moeten getallen zijn"}), 400

    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return jsonify({"error": "Deling door nul is niet mogelijk"}), 400
        result = a / b
    else:
        return jsonify({"error": f"Onbekende operatie: {operation}. Kies uit: add, subtract, multiply, divide"}), 400

    return jsonify({
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

