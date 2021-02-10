from flask import Flask, render_template, redirect, request, Blueprint
from models.attendee import Attendee

import repositories.attendee_repository as attendee_repository
import repositories.user_repository as user_repository

attendees_blueprint = Blueprint("attendees", __name__)



@attendees_blueprint.route("/user/<id>/going")
def add_festival_to_going(id):
    user =
    festival = 
    attendee = Attendee(user, festival)
    attendee_repository.save(attendee)
    return redirect("/users/<id>")


# @attendees_blueprint.route("/user/<id>/been")
# def add_festival_to_been(id):

#     return redirect("/users/<id>")