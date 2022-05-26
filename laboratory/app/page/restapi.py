import json
from typing import List

import flask.json
from flask import Blueprint

from app import db
from flask import jsonify, request
from .pharmacy import Pharmacy

module = Blueprint("restapi", __name__)


def convert_to_json(pharmacies: List[Pharmacy]) -> str:
    data = []
    for item in pharmacies:
        pharmacy = {
            "pharmacy_name": item.pharmacy_name,
            "patients_full_name": item.patients_full_name,
            "name_of_medicine": item.name_of_medicine,
            "type_of_medicine": item.type_of_medicine,
            "price_of_medicine": item.price_of_medicine,
            "county_of_origin": item.county_of_origin,
            "date_of_sale": item.date_of_sale
        }
        data.append(pharmacy)
    return flask.json.dumps(data, ensure_ascii=False)


@module.route('/get_pharmacies', methods=['GET'])
def get_pharmacies():
    pharmacies = Pharmacy.query.all()
    return convert_to_json(pharmacies)


@module.route("/delete_blog", methods=["DELETE"])
def delete_blog():
    pharmacy_id = request.args.get("pharmacy_id")
    pharmacy = Pharmacy.query.filter(Pharmacy.id == pharmacy_id).first()
    if pharmacy is not None:
        # db.session.delete(pharmacy)
        # db.session.commit()
        return jsonify({"status": "ok"})
    return jsonify({"status": "pharmacy not found"})


@module.route("/add_blog", methods=["POST"])
def add_blog():
    data = request.json
    pharmacy = Pharmacy(
        pharmacy_name=data["pharmacy_name"],
        patients_full_name=data["patients_full_name"],
        name_of_medicine=data["name_of_medicine"],
        type_of_medicine=data["type_of_medicine"],
        price_of_medicine=data["price_of_medicine"],
        county_of_origin=data["county_of_origin"],
        date_of_sale=data["date_of_sale"]
    )
    db.session.delete(pharmacy)
    db.session.commit()
    return jsonify({"status": "ok"})


@module.route("/change_blog", methods=["PUT"])
def change_blog():
    data = request.json

    pharmacy_id = data["pharmacy_id"]
    pharmacy_name = data["pharmacy_name"]
    patients_full_name = data["patients_full_name"]
    name_of_medicine = data["name_of_medicine"]
    type_of_medicine = data["type_of_medicine"]
    price_of_medicine = data["price_of_medicine"]
    county_of_origin = data["county_of_origin"]
    date_of_sale = data["date_of_sale"]

    pharmacy = Pharmacy.query.filter(Pharmacy.id == pharmacy_id).first()
    if pharmacy is None:
        return jsonify({"status": "pharmacy not found"})
    pharmacy.pharmacy_name = pharmacy_name
    pharmacy.patients_full_name = patients_full_name
    pharmacy.name_of_medicine = name_of_medicine
    pharmacy.type_of_medicine = type_of_medicine
    pharmacy.price_of_medicine = price_of_medicine
    pharmacy.county_of_origin = county_of_origin
    pharmacy.date_of_sale = date_of_sale

    db.session.commit()
    return jsonify({"status": "ok"})
