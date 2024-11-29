from flask import Blueprint, jsonify, request
import jwt
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

@user_bp.route('/profile', methods=['GET'])

def user_profile():
    token = request.headers.get('Authorization').split("Bearer ")[-1]
    
    try:
        decoded = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        print(decoded)
        accessible_resources = [
            "View Profile",
            "Update Account Details",
            "Access Personal Reports"
        ]

        return jsonify({'message': 'Welcome to the user profile!', 'accessible_resources': accessible_resources})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired, Do login again'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Login First'}), 401
