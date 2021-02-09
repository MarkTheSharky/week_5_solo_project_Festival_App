from flask import Flask, render_template, redirect, request, Blueprint
from models.festival import Festival

import repositories.festival_repository as festival_repository
import repositories.country_repository as country_repository

festivals_blueprint = Blueprint("festival", __name__)

# INDEX
@festivals_blueprint.route("/festivals")
def view_all():
    festivals = festival_repository.select_all()
    return render_template("festivals/all_festivals.html", festivals=festivals, title="All Festivals")

# SHOW

# NEW
@festivals_blueprint.route("/festivals/new", methods=['GET'])
def create_festival():
    countries = country_repository.select_all()
    return render_template("festivals/new.html", countries=countries, title="Create New Festival")

# CREATE
@festivals_blueprint.route("/festivals", methods=['POST'])
def new_festival():
    name = request.form['name']
    country = country_repository.select_by_id(request.form['country_id'])
    festival = Festival(name, country)
    festival_repository.save(festival)
    return redirect("/festivals")

# EDIT
@festivals_blueprint.route("/festivals/<id>/edit", methods=['GET'])
def edit_festival(id):
    festival = festival_repository.select_by_id(id)
    countries = country_repository.select_all()
    return render_template("festivals/edit.html", festival=festival, countries=countries, title="Edit Festival")

# UPDATE
@festivals_blueprint.route("/festivals/<id>", methods=['POST'])
def edit_festival_post(id):
    name = request.form['name']
    country = country_repository.select_by_id(request.form['country_id'])
    festival = Festival(name, country, id)
    festival_repository.update(festival)
    return redirect("/festivals")

# DELETE
@festivals_blueprint.route("/festivals/<id>/delete", methods=["POST"])
def festival_delete(id):
    festival_repository.delete_by_id(id)
    return redirect("/festivals")