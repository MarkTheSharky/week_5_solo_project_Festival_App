from flask import Flask, render_template, redirect, request, Blueprint
from models.festival import Festival

import repositories.festival_repository as festival_repository
import repositories.country_repository as country_repository

festivals_blueprint = Blueprint("festival", __name__)

# FESTIVALS HOME
@festivals_blueprint.route("/festivals")
def view_all():
    festivals = festival_repository.select_all()
    return render_template("festivals/all_festivals.html", festivals=festivals, title="All Festivals")

# CREATE NEW FESTIVAL
@festivals_blueprint.route("/festivals/create_festival", methods=['GET'])
def create_festival():
    countries = country_repository.select_all()
    return render_template("festivals/create_festival.html", countries=countries, title="Create New Festival")

# CREATE NEW FESTIVAL "POST"
@festivals_blueprint.route("/festivals", methods=['POST'])
def new_festival():
    name = request.form['name']
    country = country_repository.select_by_id(request.form['country_id'])
    festival = Festival(name, country)
    festival_repository.save(festival)
    return redirect("/festivals")

# EDIT EXISTING FESTIVAL
@festivals_blueprint.route("/festivals/edit_festival/<id>", methods=['GET'])
def edit_festival(id):
    festival = festival_repository.select_by_id(id)
    countries = country_repository.select_all()
    return render_template("festivals/edit_festival.html", festival=festival, countries=countries, title="Edit Festival")

# # EDIT EXISTING FESTIVAL "POST"
@festivals_blueprint.route("/festivals/<id>", methods=['POST'])
def edit_festival_post(id):
    name = request.form['name']
    country = country_repository.select_by_id(request.form['country_id'])
    festival = Festival(name, country, id)
    festival_repository.update(festival)
    return redirect("/festivals")