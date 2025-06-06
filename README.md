# 💰 Proxima Centauri – Fintech Record-Keeping Platform

## 📌 Project Overview

Proxima Centauri is a fintech application designed as an alternative to traditional banking, chamas, and saccos. It empowers users to manage their finances collaboratively and transparently with features for:

- Group financial management  
- Savings and deposit tracking  
- Balance status reporting  
- Role-based group membership  

---

## 📁 Project Structure

/backend
│
├── app.py # App entry point
├── extensions.py # Flask extensions initialization
├── models/ # SQLAlchemy models
│ ├── user.py
│ ├── group.py
│ ├── groupmember.py
│ └── transactions.py
├── routes/ # API Blueprints
│ ├── authentication.py
│ ├── users.py
│ ├── group.py
│ ├── groupmember.py
│ └── transactions.py
├── migrations/ # DB migration files (Alembic)
├── instance/ # Contains SQLite database (app.db)
├── requirements.txt # Required Python packages
└── README.md # This file

---

## 🧩 Models Summary

### 1. User
- Stores user credentials: `username`, `email`, `password`
- Relationships: belongs to groups, has transactions

### 2. Group
- Group name and description
- Relationships: has many members and transactions

### 3. GroupMember
- Tracks a user's role in a group (e.g., Member, Admin)
- Tracks membership date

### 4. Transaction
- Records deposits or withdrawals
- Fields: `amount`, `transaction_type`, `timestamp`

---

## 🔗 API Endpoints

### 1. Authentication

- `POST /auth/signup`  
  → Register a new user

- `POST /auth/login`  
  → Login and authenticate

---

### 2. Users

- `POST /users/`  
  → Create a new user

- `GET /users/`  
  → Get a list of all users

- `GET /users/<id>`  
  → Get user by ID

- `GET /users/username/<username>`  
  → Get user by username

- `PUT /users/<id>`  
  → Update user details (username, email, password)

- `DELETE /users/<id>`  
  → Delete a user by ID

---

### 3. Groups

- `POST /groups/`  
  → Create a new group

- `GET /groups/`  
  → List all groups

- `GET /groups/<id>`  
  → Get group by ID

- `GET /groups/name/<group_name>`  
  → Get group by name

- `PUT /groups/<id>`  
  → Update group name or description

- `DELETE /groups/<id>`  
  → Delete group by ID

- `DELETE /groups/name/<group_name>`  
  → Delete group by name

---

### 4. Group Membership

- `POST /group-members/`  
  → Add a user to a group with a specific role

- `GET /group-members/<group_name>`  
  → View all members in a specific group

- `GET /group-members/user-groups/<username>`  
  → View all groups a user is a member of

- `GET /group-members/<group_name>/<username>`  
  → View role of a user in a group

- `PUT /group-members/<group_name>/<username>`  
  → Update a user's role in the group

- `DELETE /group-members/<group_name>/<username>`  
  → Remove a user from a group

---

### 5. Transactions

- `POST /transactions/`  
  → Record a new transaction (e.g., deposit or withdrawal) for a user in a group

- `GET /transactions/<username>/<group_id>`  
  → View all transactions by a user in a group

- `GET /transactions/balance/<username>/<group_id>`  
  → View a user’s balance in a group and whether it is positive or negative

---

## 🧪 Testing

All API endpoints were tested using **Postman** with appropriate request bodies and status code validation.

---

Phase 4 Project – June 2025