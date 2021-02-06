from flask import Flask, render_template, redirect, request, Blueprint
from models.country import Country


countries_blueprint = Blueprint("country", __name__)

@countries_blueprint.route()
def 