from models import User, Group, GroupMember
from app import app
from extensions import db

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create some groups
    group1 = Group(group_name="Pamoja Group", description="Pamoja tutafanya mambo makubwa!")
    group2 = Group(group_name="Imani Womens Circle", description="Empowering women through community.")
    db.session.add_all([group1, group2])
    db.session.commit()

    # Create some users
    user1 = User(username="Joe Kimani", email="joe@example.com", password="securepassword123", group_id=group1.group_id)
    user2 = User(username="Angela Baraka", email="angela@example.com", password="anothersecurepassword", group_id=group2.group_id)

    db.session.add_all([user1, user2])
    db.session.commit()

    # Add members to group_member table
    member1 = GroupMember(user_id=user1.id, group_id=group1.group_id)
    member2 = GroupMember(user_id=user2.id, group_id=group2.group_id)
    db.session.add_all([member1, member2])
    db.session.commit()

    print("Seeding complete!")
