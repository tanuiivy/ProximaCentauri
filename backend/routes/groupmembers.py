from flask import Blueprint, request, jsonify
from extensions import db
from models.groupmembers import GroupMembers
from models.user import User
from models.group import Group

groupmembers_bp = Blueprint('groupmembers', __name__)

# Create a new group member
@groupmembers_bp.route('/', methods=['POST'])
def create_group_member():
    data = request.get_json()
    username= data.get('username')
    group_name = data.get('group_id')
    role = data.get('role', 'member')  # Default role is 'member'

   # Validate input
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group must be valid'}), 400

    # Check if the user is already a member of the group
    existing_member = GroupMembers.query.filter_by(username=username, group_name=group.group_name).first()
    if existing_member:
        return jsonify({'error': 'User is already a member of this group'}), 400

    new_member = GroupMembers(user_id=user.id, group_id=group.id, role=role)
    db.session.add(new_member)
    db.session.commit()

    return jsonify(new_member.to_dict()), 201

# Get all members of a group
@groupmembers_bp.route('/group-members/<group_name>', methods=['GET'])
def get_group_members(group_name):
    group = Group.query.filter_by(group_name=group_name).first()
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    members = GroupMembers.query.filter_by(group_id=group.id).all()
    members_data = [member.to_dict() for member in members]

    return jsonify(members_data), 200

# Get all groups a user is a member of
@groupmembers_bp.route('/user-groups/<username>', methods=['GET'])
def get_user_groups(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    group_memberships = GroupMembers.query.filter_by(user_id=user.id).all()
    groups_data = [membership.group.to_dict() for membership in group_memberships]

    return jsonify(groups_data), 200

#Update a group member's role
@groupmembers_bp.route('/group-members/<group_name>/<username>', methods=['PUT'])
def update_group_member(group_name, username):
    data = request.get_json()
    new_role = data.get('role')

    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group must be valid'}), 400

    member = GroupMembers.query.filter_by(user_id=user.id, group_id=group.id).first()
    if not member:
        return jsonify({'error': 'User is not a member of this group'}), 404
    
    member.role = new_role
    db.session.commit()
    return jsonify(member.to_dict()), 200

# Delete a group member
@groupmembers_bp.route('/group-members/<group_name>/<username>', methods=['DELETE'])
def delete_group_member(group_name, username):
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group must be valid'}), 400

    member = GroupMembers.query.filter_by(user_id=user.id, group_id=group.id).first()
    if not member:
        return jsonify({'error': 'User is not a member of this group'}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'}), 200