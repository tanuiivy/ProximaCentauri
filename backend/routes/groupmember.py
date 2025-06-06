from flask import Blueprint, request, jsonify
from extensions import db
from models.groupmember import GroupMember
from models.user import User
from models.group import Group

groupmember_bp = Blueprint('groupmember', __name__)

# Create a new group member
@groupmember_bp.route('/', methods=['POST'])
def create_group_member():
    data = request.get_json()
    username= data.get('username')
    group_name = data.get('group_name')
    role = data.get('role', 'Member')  # Default role is 'member'

   # Validate input
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group not found'}), 400

    # Check if the user is already a member of the group
    existing_member = GroupMember.query.filter_by(user_id=user.id, group_id=group.group_id).first()
    if existing_member:
        return jsonify({'error': 'User is already a member of this group'}), 400

    new_member = GroupMember(user_id=user.id, group_id=group.group_id, role=role)
    db.session.add(new_member)
    db.session.commit()

    return jsonify(new_member.to_dict()), 201

# Get all members of a group
@groupmember_bp.route('/<group_name>', methods=['GET'])
def get_group_members(group_name):
    group = Group.query.filter_by(group_name=group_name).first()
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    members = GroupMember.query.filter_by(group_id=group.group_id).all()
    members_data = [member.to_dict() for member in members]

    return jsonify(members_data), 200

# Get all groups a user is a member of
@groupmember_bp.route('/<username>', methods=['GET'])
def get_user_groups(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    group_memberships = GroupMember.query.filter_by(user_id=user.id).all()
    groups_data = [membership.group.to_dict() for membership in group_memberships]

    return jsonify(groups_data), 200

# Get a specific member's role in a group
@groupmember_bp.route('/<group_name>/<username>', methods=['GET'])
def get_member_role(group_name, username):
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()
    if not user or not group:
        return jsonify({'error': 'User or Group not found'}), 404

    member = GroupMember.query.filter_by(user_id=user.id, group_id=group.group_id).first()
    if not member:
        return jsonify({'error': f'{username} is not a member of {group_name}'}), 404

    return jsonify({
        'username': username,
        'group': group_name,
        'role': member.role,
        'joined_at': member.joined_at
    }), 200

#Update a group member's role
@groupmember_bp.route('/<group_name>/<username>', methods=['PUT'])
def update_group_member(group_name, username):
    data = request.get_json()
    new_role = data.get('role')

    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group must be valid'}), 400

    member = GroupMember.query.filter_by(user_id=user.id, group_id=group.group_id).first()
    if not member:
        return jsonify({'error': 'User is not a member of this group'}), 404
    
    member.role = new_role
    db.session.commit()
    return jsonify(member.to_dict()), 200

# Delete a group member
@groupmember_bp.route('/<group_name>/<username>', methods=['DELETE'])
def delete_group_member(group_name, username):
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

    if not user or not group:
        return jsonify({'error': 'User and Group must be valid'}), 400

    member = GroupMember.query.filter_by(user_id=user.id, group_id=group.group_id).first()
    if not member:
        return jsonify({'error': 'User is not a member of this group'}), 404

    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member deleted successfully'}), 200