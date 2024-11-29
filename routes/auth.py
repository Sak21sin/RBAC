from flask import Blueprint, request, jsonify
from models import db, User
from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth', __name__)
blacklisted_tokens = set()

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
  
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400
    if not username or not password or not role:
        return jsonify({'message': 'username or password cannot be empty'})
    
    user = User(username=username, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    print(user)
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Generate a JWT token for the user including the role
    payload = {
        'username':username,
        'user_id': user.id,
        'role': user.role,  
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiry
    }
    token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')

    return jsonify({'message': f'Login successful {username}', 'token': token, 'username':username})


@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization').split("Bearer ")[-1]
    try:
        decoded = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        # Add token to the blacklist
        blacklisted_tokens.add(token)

        return jsonify({'message': 'Logged out successfully'})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

@auth_bp.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('Authorization').split("Bearer ")[-1]
    try:
        # Check if the token is blacklisted
        if token in blacklisted_tokens:
            return jsonify({'error': 'Token is invalidated. Please log in again.'}), 401

        decoded = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        return jsonify({'message': 'Access granted', 'user': decoded})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401