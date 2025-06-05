from flask import Blueprint, request, jsonify
from extensions import db
from models.group import Group
from routes.users import users_bp

groups_bp = Blueprint('groups', __name__)

#Create a new group
@groups_bp.route('/', methods=['POST'])
def create_group():
    data = request.get_json()
    group_name = data.get('name')
    description = data.get('description')

    if not group_name:
        return jsonify({'error': 'Group name is required'}), 400

    if Group.query.filter_by(group_name=group_name).first():
        return jsonify({'error': 'Group name already exists'}), 400

    new_group = Group(group_name=group_name, description=description)
    db.session.add(new_group)
    db.session.commit()
    
    return jsonify(new_group.to_dict()), 201

# Get all groups
@groups_bp.route('/', methods=['GET'])
def get_groups():
    groups = Group.query.all()
    groups_data = [group.to_dict() for group in groups]
    return jsonify(groups_data), 200

# Get a group by ID
@groups_bp.route('/<int:group_id>', methods=['GET'])
def get_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    return jsonify(group.to_dict()), 200

#Get a group by name
@groups_bp.route('/name/<string:group_name>', methods=['GET'])
def get_group_by_name(group_name):
    group = Group.query.filter_by(group_name=group_name).first()
    if not group:
        return jsonify({'error': 'Group not found'}), 404
    return jsonify(group.to_dict()), 200

# Update a group
@groups_bp.route('/<int:group_id>', methods=['PUT'])
def update_group(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    data = request.get_json()
    group.group_name = data.get('name', group.group_name)
    group.description = data.get('description', group.description)

    db.session.commit()
    return jsonify(group.to_dict()), 200

#Delete group by id
@groups_bp.route('/<int:group_id>', methods=['DELETE'])
def delete_group_by_id(group_id):
    group = Group.query.get(group_id)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    db.session.delete(group)
    db.session.commit()
    return jsonify({'message': 'Group deleted successfully'}), 200

# Delete a group
@groups_bp.route('/name/<string:group_name>', methods=['DELETE'])
def delete_group(group_name):
    group = Group.query.filter_by(group_name=group_name).first()
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    db.session.delete(group)
    db.session.commit()
    return jsonify({'message': 'Group deleted successfully'}), 200