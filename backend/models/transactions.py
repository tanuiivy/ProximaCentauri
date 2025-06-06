from extensions import db
from sqlalchemy_serialization import SerializerMixin
from datetime import datetime

class Transaction(db.Model, SerializerMixin):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)  
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', back_populates='transactions')
    group = db.relationship('Group', back_populates='transactions')

    serialize_rules =('-user.password')

    def __repr__(self):
        return f'<Transaction {self.id} - {self.transaction_type} - {self.amount}>'