from flask import Flask, render_template, redirect, request, Blueprint
from models.attendee import Attendee
from models.user import User
from models.festival import Festival

import repositories.attendee_repository as attendee_repository
import repositories.user_repository as user_repository
import repositories.festival_repository as festival_repository


attendees_blueprint = Blueprint("attendees", __name__)



@attendees_blueprint.route("/users/<id>/going", methods=['POST'])
def add_festival_to_going(id):
    user = user_repository.select_by_id(id)
    festival_id = request.form['festivals_going']
    festival = festival_repository.select_by_id(festival_id)
    attendee = Attendee(user, festival)
    attendee_repository.save(attendee)
    return redirect("/users")