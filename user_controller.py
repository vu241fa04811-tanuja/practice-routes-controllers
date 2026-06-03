from flask import jsonify, request
from bson.objectid import ObjectId
from db import db

user_collection=db["users"]

def get_users():
    users=[]
    user_list=user_collection.find()
    for user in user_list:
        user["_id"]=str(user["_id"])
        users.append(user)
    return jsonify(users)

def add_user():
    data=request.get_json()
    user= {
        "name":data.get("name"),
        "email":data.get("email")
    }
    user_collection.insert_one(user)
    return "Users Inserted Succesfully"
    return jsonify(data)

def get_user_byID(id):
    user=user_collection.find_one(ObjectId(id))
    if user:
        user["_id"]=str(user["_id"])
        return jsonify(user)    
    return jsonify({"message": "User not found"})

def delete_user(id):
    user_collection.delete_one({"_id":ObjectId(id)})
    return jsonify({"message":"user deleted successfully"})
    #return jsonify({"message": "User not found"})

def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            return jsonify({"message": "User updated successfully"})
    return jsonify({"message": "User not found"})