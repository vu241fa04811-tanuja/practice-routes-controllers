from flask import jsonify, request
from bson.objectid import ObjectId
from db import db

product_collection = db["products"]


def get_products():
    products = []
    product_list = product_collection.find()

    for product in product_list:
        product["_id"] = str(product["_id"])
        products.append(product)

    return jsonify(products)



def add_product():
    data = request.get_json()

    product = {
        "name": data.get("name"),
        "price": data.get("price"),
        "category": data.get("category")
    }

    product_collection.insert_one(product)
    return jsonify({"message": "Product inserted successfully"})



def get_product_byID(id):
    product = product_collection.find_one({"_id": ObjectId(id)})

    if product:
        product["_id"] = str(product["_id"])
        return jsonify(product)

    return jsonify({"message": "Product not found"})



def delete_product(id):
    product_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Product deleted successfully"})


def update_product(product_id):
    data = request.get_json()

    product_collection.update_one(
        {"_id": ObjectId(product_id)},
        {"$set": {
            "name": data.get("name"),
            "price": data.get("price"),
            "category": data.get("category")
        }}
    )

    return jsonify({"message": "Product updated successfully"})