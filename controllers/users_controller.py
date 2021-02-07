from flask import Flask, render_template, redirect, request, Blueprint
from models.user import User
from models.festival import Festival

import repositories.user_repository as user_repository
import repositories.festival_repository as festival_repository

users_blueprint = Blueprint("users", __name__)

# View all users
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("users/users.html", users=users)

# View user page
@users_blueprint.route("/users/<id>", methods=['GET'])
def user_page(id):
    user = user_repository.select_by_id(id)
    festivals = festival_repository.select_all()
    return render_template("/users/user.html", user=user, festivals=festivals)