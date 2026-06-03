from flask import jsonify, request
from bson.objectid import ObjectId
from db import db

# MongoDB Collection
carts_collection = db["carts"]


# GET ALL CARTS
def get_carts():

    carts = []

    carts_list = carts_collection.find()

    for cart in carts_list:

        cart["_id"] = str(cart["_id"])

        carts.append(cart)

    return jsonify(carts)


# ADD NEW CART
def add_carts():

    data = request.get_json()

    cart = {
        "name": data.get("name"),
        "price": data.get("price"),
        "category": data.get("category")
    }

    carts_collection.insert_one(cart)

    return jsonify({"message": "Cart inserted successfully"})


# GET CART BY ID
def get_carts_byID(id):

    cart = carts_collection.find_one({"_id": ObjectId(id)})

    if cart:

        cart["_id"] = str(cart["_id"])

        return jsonify(cart)

    return jsonify({"message": "Cart not found"})


# DELETE CART
def delete_carts(id):

    carts_collection.delete_one({"_id": ObjectId(id)})

    return jsonify({"message": "Cart deleted successfully"})


# UPDATE CART
def update_carts(id):

    data = request.get_json()

    carts_collection.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": data.get("name"),
                "price": data.get("price"),
                "category": data.get("category")
            }
        }
    )

    return jsonify({"message": "Cart updated successfully"})