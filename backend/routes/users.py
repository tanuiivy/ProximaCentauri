from flask import Blueprint,  request, jsonify 
from extensions import db
from models.user import User

users_bp = Blueprint('users', __name__)

#Create a new user
@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Validation
    if not username or not email or not password:
        return jsonify({'error': 'Missing username, email, or password'}), 400

    # Check if user already exists
    if User.query.filter((User.username == username)).first():
        return jsonify({'error': 'Username already exists'}), 400

    # Create a new user
    new_user = User(username=username, email=email, password=password)

    # Add to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

#Get all users
@users_bp.route('/', methods=['GET'])
def get_all_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Get user by ID
@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

#Get user by username
@users_bp.route('/username/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# Update user information
@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # Update fields if provided
    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.password = password

    db.session.commit()
    return jsonify(user.to_dict()), 200

# Delete user
@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {user.username} deleted successfully'}), 200