from flask import Blueprint, jsonify, request
from src.repositors.user import UserRepositor
import json


user  = Blueprint("user", __name__, url_prefix="/api/v1/user")
user_repo = UserRepositor()


@user.route(rule="/", methods=["POST"])
def Register():
    nome = request.json["nome"]
    ativo = request.json["ativo"]
    
    id = user_repo.insert(nome, ativo)
    user_created = user_repo.select_by_id(id)
    print(user_created)
    
    return jsonify({"user":user_created}), 201
    
@user.route(rule="/", methods=["GET"])
def get_all_users():
    users = user_repo.select()
    return jsonify({"users": users}), 200


@user.route(rule="/<id>", methods=["GET"])
def get_one_user_by_id(id):
    user = user_repo.select_by_id(id)
    return jsonify({"user": user})


@user.route(rule="/<id>", methods=["PUT"])
def delete(id):
    nome  = request.json["nome"]
    user_repo.update(id, nome)
    user_updated = user_repo.select_by_id(id)
    return jsonify(user_updated), 200
    
    
@user.route(rule="/<id>", methods=["DELETE"])
def update(id):
    user_repo.delete(id)
    return  jsonify(), 204