from flask import Flask, render_template, redirect, request, Blueprint
from models.festival import Festival


festivals_blueprint = Blueprint("festival", __name__)