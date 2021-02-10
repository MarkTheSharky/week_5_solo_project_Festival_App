from flask import Flask, render_template, redirect, request, Blueprint
from models.attendees import Attendees



attendees_blueprint = Blueprint("attendees", __name__)

