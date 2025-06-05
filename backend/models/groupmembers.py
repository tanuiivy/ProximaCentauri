from extensions import db
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

class GroupMembers(db.Model, SerializerMixin):
    __tablename__ = 'group_members'

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.group_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='Member')  
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    group = db.relationship('Group', back_populates='groupmembers')
    user = db.relationship('User', back_populates='groupmembers')

    def __repr__(self):
        return f"<GroupMembers {self.user_id} in Group {self.group_id}>"