from flask import Blueprint, render_template, jsonify,request
# from models import Category  # Asegúrate de que la ruta sea correcta.
from bd_config import db

from logging import Logger

# Definir el Blueprint correctamente
bp = Blueprint('category', __name__, url_prefix='/category')

bp.route('/', methods=['POST'])
def add_group():
    data  = request.get_json()
    if data:
        message,new_group,code = utils.validate_json(data,"group")
        if code != 200:
            return jsonify({"message": f"{message}"}),code
        else:
           save_group = GroupService.save_group(new_group)
           db.session.commit()
           return jsonify({"message": f"{save_group}"}),code
bp.route('/', methods=['GET'])
def get_all_groups():
    groups =  Group.get_all_groups()
    if groups:
        return jsonify([{"id": e.id, "Name": e.group_name,"Nivel": e.group_level, "Capacidad": e.group_capacity} for e in db.session.query(Group).all()]),200        
