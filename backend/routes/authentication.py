from flask import Blueprint, request, jsonify #blueprint allows for modular routing instead of all routes in app.py: request allows access to form data:jsonify converts dictionaries into JSON responses
from extensions import db
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash #generate_password_hash converts password into hashed version before saving: check_password_hash compare hashed with plain text

authentication_bp = Blueprint('authentication', __name__)
#signup
@authentication_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    #validation
    if not username or not email or not password:
        return jsonify({'error': 'Missing username, email, or password'}), 400

    #password length check
    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters long'}), 400

    #to see if user exists
    if User.query.filter((User.username == username)).first():
        return jsonify({'error': 'Username already exists'}), 400

    #hash the password
    hashed_password = generate_password_hash(password)

    #create a new user
    new_user = User(username=username, email=email, password=hashed_password)

    #add to the db
    db.session.add(new_user)
    db.session.commit()

    #return a success message
    return jsonify({'message': 'User created successfully'}), 201
#login
@authentication_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    #validation
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    #find the user
    user = User.query.filter((User.username == username)).first()

    #check if user exists and password matches
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    #return a success message
    return jsonify({'message': f'Login successful: {user.username}!'}), 200
