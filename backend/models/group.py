from extensions import db
from sqlalchemy_serializer import SerializerMixin

class Group(db.Model, SerializerMixin):
    __tablename__ = 'groups'

    group_id = db.Column(db.Integer, primary_key=True)
    group_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    users = db.relationship('User', backref='group', lazy=True)
    groupmember= db.relationship('GroupMember', back_populates='group', lazy=True)

    serialize_rules = ('-users', '-groupmember')

    def __repr__(self):
        return f"<Group {self.group_name}>"