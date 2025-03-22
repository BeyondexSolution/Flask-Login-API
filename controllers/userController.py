import logging
from flask import Flask, request, jsonify
import jwt
import datetime
from models.models import GigiCmsLogin  # Import the updated User model
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
#from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
def login():
    # return "Welcome to my Flask API!"
    """Authenticate user and return JWT token"""

    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return jsonify({"message": "Username and password are required"}), 400  # Bad request error

        # Query the user from the database
        user = GigiCmsLogin.query.filter_by(GL_USERNAME=username,GL_PASSWORD=password).first()

        if user:  # Secure password check
            token = jwt.encode(
                {
                    "user_id": user.GL_RECID,
                    "role": user.GL_ROLE,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # Adjust expiration as needed
                },
                SECRET_KEY,
                algorithm="HS256"
            )
            data={
                "RecordID":user.GL_RECID,
                "UserName":user.GL_USERNAME,
                "Role":user.GL_ROLE,
                #"SECRET_KEY":SECRET_KEY
            }
            return jsonify({"status": "Y","token": token, "data": data,"msg":"Login Successfully"}), 200

        return jsonify({"status": "N","msg": "Invalid credentials"}), 401
    except Exception as e:
        logging.error(f"Error occurred in http_example route: {e}")
        return jsonify({"status": "N","msg": f"An error occurred in the request: {str(e)}"}), 500
    
def get_all_users():
    doctors = GigiCmsLogin.query.all()
    return [user_to_dict(doc) for doc in doctors]

def user_to_dict(doctor):
    return {
        'RecordID': doctor.GL_RECID,
        'Username': doctor.GL_USERNAME,
        'Password': doctor.GL_PASSWORD,
        'Role': doctor.GL_ROLE,
    }
