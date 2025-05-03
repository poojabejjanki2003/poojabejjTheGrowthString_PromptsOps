from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operator = data['operator']

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Division by zero'}), 400
    else:
        return jsonify({'error': 'Invalid operator'}), 400

    return jsonify({'result': result})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)