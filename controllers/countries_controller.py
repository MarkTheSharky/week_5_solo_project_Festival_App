from flask import Flask, render_template, redirect, request, Blueprint
from models.country import Country

import repositories.country_repository as country_repository
import repositories.festival_repository as festival_repository

countries_blueprint = Blueprint("country", __name__)

@countries_blueprint.route("/countries", methods=['GET'])
def view_all():
    countries = country_repository.select_all()
    festivals = festival_repository.select_all()
    return render_template("countries/countries.html", countries=countries, festivals=festivals, title="Browse By Country")

# @countries_blueprint.route