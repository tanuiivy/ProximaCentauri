from flask import Blueprint, request, jsonify
from extensions import db
from models.transactions import Transaction
from models.user import User
from models.group import Group

transactions_bp = Blueprint('transactions', __name__)

#Add a new transaction
@transactions_bp.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    username = data.get('username')
    group_name = data.get('group_name')
    amount = data.get('amount')
    transaction_type = data.get('transaction_type')

    # Validate the user exists
    if not username or not group_name or not amount or not transaction_type:
        return jsonify({'error': 'Missing required fields'}), 400

    user = User.query.filter_by(username=username).first()
    group = Group.query.filter_by(group_name=group_name).first()

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