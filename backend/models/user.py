from extensions import db
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(117), nullable=False)

    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'), nullable=True)
    groupmember = db.relationship('GroupMember', back_populates='user', lazy=True)
    transactions = db.relationship('Transaction', back_populates='user', lazy=True)

    serialize_rules = ('-groupmember', '-password', '-transactions.user')

def __repr__(self):
    return f"<User {self.username}>"