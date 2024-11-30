from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users:
        return jsonify({"error": "User already exists!"}), 400
    users[username] = password
    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if users.get(username) == password:
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"error": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

