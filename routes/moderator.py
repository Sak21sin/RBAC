from flask import Blueprint, jsonify, request
import jwt

moderator_bp = Blueprint('moderator', __name__)

@moderator_bp.route('/moderator_dashboard', methods=['GET'])
def moderator_dashboard():
    token = request.headers.get('Authorization').split("Bearer ")[-1]
    
    try:
        decoded = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        print(decoded)
        if decoded.get('role') != 'moderator' and decoded.get('role') != 'admin':
            return jsonify({'error': 'Access denied'}), 403
        accessible_resources = [
            "View Profile",
            "Update Account Details",
            "Access Personal Reports", 'Manage Content'
        ]

        return jsonify({'message': 'Welcome to the Moderator dashboard of VRV Security!', 'accessible_resources': accessible_resources})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Login First'}), 401
