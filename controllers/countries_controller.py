from flask import Flask, render_template, redirect, request, Blueprint
from models.country import Country

import repositories.country_repository as country_repository
import repositories.festival_repository as festival_repository

countries_blueprint = Blueprint("country", __name__)

# INDEX
@countries_blueprint.route("/countries", methods=['GET'])
def view_all():
    countries = country_repository.select_all()
    festivals = festival_repository.select_all()
    return render_template("countries/countries.html", countries=countries, festivals=festivals, title="Browse By Country")

# SHOW

# NEW
@countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    return render_template("countries/new.html")

# CREATE
@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["country_name"]
    code = request.form["country_code"]
    country = Country(name, code)
    country_repository.save(country)
    return redirect("/countries")

# EDIT
@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select_by_id(id)
    return render_template("countries/edit.html", country=country)

# UPDATE
@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form["country_name"]
    code = request.form["country_code"]
    country = Country(name, code.upper(), id)
    country_repository.update(country)
    return redirect("/countries")

# DELETE
@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete_by_id(id)
    return redirect("/countries")