from flask import Flask, render_template, redirect, request, Blueprint
from models.festival import Festival

import repositories.festival_repository as festival_repository
import repositories.country_repository as country_repository

festivals_blueprint = Blueprint("festival", __name__)

@festivals_blueprint.route("/festivals", methods=['GET'])
def view_all():
    festivals = festival_repository.select_all()
    return render_template("festivals/all_festivals.html", festivals=festivals, title="All Festivals")

# @festivals_blueprint.route("/festivals/<name>", methods=['GET'])
# def view_festival(name):
#     #take name and get id from it
#     festival = festival_repository.select_by_id()
#     return render_template("festivals/festival.html", festival=festival)

# CREATE NEW FESTIVAL
@festivals_blueprint.route("/create_festival", methods=['GET'])
def create_festival():
    countries = country_repository.select_all()
    return render_template("festivals/create_festival.html", countries=countries, title="Create New Festival")

# ADD NEW FESTIVAL
@festivals_blueprint.route("/festival", methods=['POST'])
def new_festival():

    return redirect("/festivals")