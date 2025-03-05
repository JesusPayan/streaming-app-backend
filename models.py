from flask import Flask, jsonify
from bd_config import db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Date, create_engine
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from contextlib import contextmanager
from sqlalchemy import engine, create_engine
import mysql.connector

# No es necesario declarar Base si se usa db.Model

#class Role(db.Model):  # Cambié db.model a db.Model
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer, primary_key=True)  # Cambié db.column a db.Column
#    role_name = db.Column(db.String(40), nullable=False)  # Cambié roleName a role_name para seguir la convención
#    users = relationship("User", back_populates="role")  # Cambié el nombre de la relación a users

from main import db
# def get_db() -> SQLAlchemy:
#     global __db__
#     if not __db__:
#         __db__ = SQLAlchemy(engine_options = {"insolation_level": "AUTOCOMMIT"})
#     return __db__
# def get_db_direct() -> engine:
#     global _dbDirect_
#     if not _dbDirect_:
#         _dbDirect_ = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'],
#                                      execution_options={"isolation_level": "AUTOCOMMIT"})
#     return _dbDirect_


# def get_db_direct_dirty() -> engine:
#     global _dbDirectDirtyRead_
#     if not _dbDirectDirtyRead_:
#         _dbDirectDirtyRead_ = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'],
#                                               execution_options={"isolation_level": "READ UNCOMMITTED"})
#     return _dbDirectDirtyRead_




# @contextmanager
# def open_db_connection(commit=False):
#     connection_engine = get_db_direct()
#     if commit == False:
#         #connectionEngine.execution_options(isolation_level="READ UNCOMMITTED")
#         connection = connection_engine.raw_connection()
#         cursor = connection.cursor()
#         #connection = connectionEngine.connect()
#         try:
#             yield cursor
#         except Exception as inst:
#             # the exception instance
#             # logger.log_text(str(inst), severity="ERROR")
#             print(str(inst))
#             raise inst
#         finally:
#             connection.close()
#     else:
#         # with connectionEngine.begin() as connection:
#         try:
#             yield connection_engine
#             connection_engine.execute("COMMIT")
#         except Exception as inst:
#             # the exception instance
#             # logger.log_text(str(inst), severity="ERROR")
#             connection_engine.execute("ROLLBACK")
#     raise inst
# conn = ''

# conn = mysql.connector.connect(host="localhost", user="root", password="root", database="streaming_db_dev")




class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    def save_newn_role(role):
        try:
            db.session.add(role)
            db.session.commit()
        except Exception as e:
            print(e)
    @staticmethod 
    def getroles() -> list:
        results_list = []
        query_results = db.session.query(Role).all()

        if query_results:
            for result in query_results:
                print(result)
                role = Role(id = result.id,name = result.name)
                results_list.append(role)

        return results_list   
        
class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    cellphone = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('Role.id'), nullable=False)
    # role = db.relationship('Role', backref=db.backref('users', lazy=True))
class plataform(db.Model):
    __tablename__ = 'plataform'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    maximum_users = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    screen_cost_for_users = db.Column(db.Float, nullable=False)
    screen_cost = db.Column(db.Float, nullable=False)
    account_cost_for_users = db.Column(db.Float, nullable=False)
    account_cost = db.Column(db.Float, nullable=False)
    plataform_status = db.Column(db.String(50), nullable=False)
class account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    account_email = db.Column(db.String(50), nullable=False)
    account_password = db.Column(db.String(50), nullable=False)
    available_screen = db.Column(db.Integer, nullable=False)
    bought_date = db.Column(db.String(50), nullable=False)
    plataform_id = db.Column(db.Integer, db.ForeignKey('plataform.id'), nullable=False)
    # plataform = db.relationship('plataform', backref=db.backref('accounts', lazy=True))
class payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.String(50), nullable=False)
    next_payment_date = db.Column(db.String(50), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('user', backref=db.backref('payments', lazy=True))

class subscription(db.Model):
    __tablename__ = 'subscription'
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.String(50), nullable=False)
    end_date = db.Column(db.String(50), nullable=False)
    total_cost = db.Column(db.Float, nullable=False)
    subscription_status = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('user', backref=db.backref('subscriptions', lazy=True))
    payment_id = db.Column(db.Integer, db.ForeignKey('payment.id'), nullable=False) 
    # payment = db.relationship('payment', backref=db.backref('subscriptions', lazy=True))
class subscripcion_details(db.Model):
    __tablename__ = 'subscripcion_details'
    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscription.id'), nullable=False)
    subscription = db.relationship('subscription', backref=db.backref('subscripcion_details', lazy=True))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    # account = db.relationship('account', backref=db.backref('subscripcion_details', lazy=True))
    subscripcion_details_cost = db.Column(db.Float, nullable=False)
    
db.create_all()


