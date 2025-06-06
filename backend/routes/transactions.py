from flask import Blueprint, request, jsonify
from extensions import db
from models.transactions import Transaction
from models.user import User
from models.group import Group

transactions_bp = Blueprint('transactions', __name__)

#Add a new transaction
@transactions_bp.route('/', methods=['POST'])
def create_transaction():
    data = request.get_json()
    username = data.get('username')
    group_id = data.get('group_id')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')

    # Validate the user exists
    if not username or not group_id or not amount or not transaction_type:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_id=group_id).first()

    if not user or not group:
        return jsonify({'error': 'User or Group not found'}), 404

    #Creating the transaction
    transaction = Transaction(
        user_id=user.id,
        group_id=group.id,
        amount=amount,
        transaction_type=transaction_type
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify(transaction.serialize()), 201

# Get all transactions from a user in a group
@transactions_bp.route('/<username>/<group_id>', methods=['GET'])
def get_user_transactions(username, group_id):
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_id=group_id).first()

    if not user or not group:
        return jsonify({'error': 'User or Group not found'}), 404

    transactions = Transaction.query.filter_by(user_id=user.id, group_id=group.id).all()

    return jsonify([transaction.serialize() for transaction in transactions]), 200

#Get user balance in a group
@transactions_bp.route('/balance/<username>/<group_id>', methods=['GET'])
def get_user_balance(username, group_id):
    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_id=group_id).first()

    if not user or not group:
        return jsonify({'error': 'User or Group not found'}), 404

    transactions = Transaction.query.filter_by(user_id=user.id, group_id=group.id).all()
    balance = sum(t.amount for t in transactions)

    if balance > 0:
        message = f"Positive balance of {balance} saved in group {group.group_name}."
    elif balance < 0:
        message = f"Negative balance of {balance} owed in group {group.group_name}."
    else:
        message = f"No balance in group {group.group_name}."

    return jsonify({'username': username, 'group': group.group_name, 'balance': balance, 'message': message}), 200