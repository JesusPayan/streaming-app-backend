from flask import Blueprint,request,jsonify
from main import app,db
from models import Role


rolebp = Blueprint('role', __name__, url_prefix='/role')

@rolebp.route('/', methods=['GET'])
def get_all_roles():
    r = Role.getroles()
    
    return jsonify([{"id": e.id, "name": e.name} for e in r]),200
@rolebp.route('/', methods=['POST'])
def add_role():
    data  = request.get_json()
    if data:
        print(data)
        if data['role_name']!='':
            create_role(data['role_name'])
            return jsonify({"message": f"se agrego el rol {data['role_name']} correctamente"}),201 
        else:
            return jsonify({"message": f"!El campo Rol no puede estar vacio¡"}),201
def create_role(name):  
    new_role = role(name=name)
    try:
        db.session.add(new_role)
        db.session.flush()
        db.session.commit()
       
    except Exception as e:
        print(e)
        return jsonify({"message": f"Hubo un error al agregar el rol {name} "}),201

