from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        full_name = data.get('full_name')
        dob = data.get('dob')
        email = data.get('email')
        roll_number = data.get('roll_number')
        numbers = [i for i in data.get('array', []) if isinstance(i, int)]
        alphabets = [i for i in data.get('array', []) if isinstance(i, str) and i.isalpha()]

        response = {
            "status": "success",
            "user_id": f"{full_name.replace(' ', '_')}_{dob}",
            "college_email_id": email,
            "college_roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "is_success": True
        }
    except Exception as e:
        response = {
            "status": "error",
            "is_success": False,
            "message": str(e)
        }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
