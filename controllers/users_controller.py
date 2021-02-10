from flask import Flask, render_template, redirect, request, Blueprint
from models.user import User
from models.festival import Festival

import repositories.user_repository as user_repository
import repositories.festival_repository as festival_repository
import repositories.attendee_repository as attendee_repository

users_blueprint = Blueprint("users", __name__)

# INDEX - VIEW ALL USERS
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/users.html", users=users)

# SHOW
@users_blueprint.route("/users/<id>", methods=["GET"])
def user(id):
    user = user_repository.select_by_id(id)
    festivals = festival_repository.select_all()
    attendees = attendee_repository.select_all()
    return render_template("users/user.html", user=user, festivals=festivals, attendees=attendees)

# NEW
@users_blueprint.route("/users/new")
def new_user():
    return render_template("users/new.html", title="create users")

# CREATE
@users_blueprint.route("/users", methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]
    user = User(first_name, last_name, age)
    user_repository.save(user)
    return redirect("/users")

# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repository.select_by_id(id)
    return render_template("users/edit.html", user=user)

# UPDATE
@users_blueprint.route("/users/<id>", methods=["POST"])
def update_user(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]
    user = User(first_name, last_name, age, id)
    user_repository.update(user)
    return redirect("/users")

# DELETE
@users_blueprint.route("/users/<id>/delete", methods=["POST"])
def user_delete(id):
    user_repository.delete_by_id(id)
    return redirect("/users")

