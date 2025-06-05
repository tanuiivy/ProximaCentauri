💰 Proxima Centauri – Fintech Record-Keeping Platform
# Project Overview
Proxima Centauri is a fintech application designed as an alternative to traditional banking, chamas, and saccos. It empowers users to manage their finances collaboratively and transparently with features for group financial management, savings tracking, and loan management.

# Project Structure
/backend
│
├── app.py # App entry point
├── extensions.py # Contains Flask extension initializations
├── models/
│ ├── user.py
│ ├── group.py
│ └── groupmember.py
├── routes/
│ ├── authentication.py
│ ├── users.py
│ ├── group.py
│ └── groupmember.py
├── migrations/ # DB migration files
├── requirements.txt # Required packages
└── instance/ # Contains app.db (SQLite file)

### Models

1. **User Model**
   - Stores user credentials and basic info
   - Relationships: Belongs to groups, has group memberships

2. **Group Model**
   - Stores group information
   - Relationships: Has many users and memberships

3. **GroupMember Model**
   - Junction table with additional attributes
   - Tracks roles and join dates

# API ENDPOINTS
1. **Authentication**
POST /auth/signup
→ Register a new user

POST /auth/login
→ Login and authenticate
2.  **Users** 
POST /users/
→ Create a new user

GET /users/
→ Get a list of all users

GET /users/<id>
→ Get user by their unique ID

GET /users/username/<username>
→ Get user by username

PUT /users/<id>
→ Update user details (username, email, password)

DELETE /users/<id>
→ Delete a user by ID

3. **Group**
POST /groups/
→ Create a new group

GET /groups/
→ List all groups

GET /groups/<id>
→ Get group by ID

GET /groups/name/<group_name>
→ Get group by name

PUT /groups/<id>
→ Update group name or description

DELETE /groups/<id>
→ Delete group by ID

DELETE /groups/name/<group_name>
→ Delete group by name

4. **Group Membership**
POST /group-members/
→ Add a user to a group with a specific role

GET /group-members/<group_name>
→ View all members in a specific group

GET /group-members/user-groups/<username>
→ View all groups a user is a member of

PUT /group-members/<group_name>/<username>
→ Update a member's role in the group

DELETE /group-members/<group_name>/<username>
→ Remove a user from a group

## Testing done with postman ##