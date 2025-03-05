from bd_config import app,db
import os
from flask import json,jsonify,request
from app.routes import Role
from app.routes import Category

#app.register_blueprint(student_api)
# app.register_blueprint(Role)
app.register_blueprint(Role.rolebp)
app.register_blueprint
# @app.route('/')
def home():
     return jsonify({"message": "Bienvenido a la API de Streaming"}),200
if __name__ == "__main__":
    db.create_all()
    app.app_context().push()
    app.run(debug=True)