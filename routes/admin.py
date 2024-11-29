from flask import Blueprint, jsonify, request
import jwt

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard', methods=['GET'])
def admin_dashboard():
    token = request.headers.get('Authorization').split("Bearer ")[-1]
    
    try:
        decoded = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
        print(decoded)
        role = decoded.get('role')
        if role != 'admin':
            return jsonify({'error': 'Access denied'}), 403
        
        accessible_resources = [
            "Manage Users",
            "View Admin Logs",
            "Edit System Settings",
            "Monitor Security Events",
            "Generate Reports"
        ]

        return jsonify({'message': 'Welcome to the admin dashboard of VRV Security!', 'accessible_resources': accessible_resources})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Login First'}), 401
