from flask import Flask, send_from_directory, request, jsonify
import jwt
import datetime

app = Flask(__name__, static_folder='../client', template_folder='../client')
app.config['SECRET_KEY'] = '3f634c2f4af85823d64392a5c162c72ccf031f57df905ea8c5c010647d3a9c51'

# Load users from a file
def load_users(file_path="users.txt"):
    users = {}
    try:
        with open(file_path, "r") as f:
            for line in f:
                username, password = line.strip().split(":")
                users[username] = password
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please create it with username:password pairs.")
    return users

USERS = load_users()

@app.route('/')
def index():
    return send_from_directory('../client', 'login.html')  # Serve login page from the client folder

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in USERS and USERS[username] == password:
        token = jwt.encode(
            {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            app.config['SECRET_KEY'], algorithm="HS256"
        )
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/home')
def home():
    return send_from_directory('../client', 'home.html')  # Serve home page from the client folder

@app.route('/client/<path:filename>')
def static_files(filename):
    return send_from_directory('../client', filename)  # Serve CSS/JS files

@app.route('/validate', methods=['POST'])
def validate():
    token = request.json.get('token')
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({'message': 'Token is valid', 'user': decoded['user']})
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Invalid token'}), 401

if __name__ == '__main__':
    if not USERS:
        print("No users found. Please check your users.txt file.")
    app.run(debug=True)
