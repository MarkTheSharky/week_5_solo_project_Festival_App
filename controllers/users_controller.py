from flask import Flask, render_template, redirect, request, Blueprint
from models.user import User

import repositories.user_repository as user_repository

users_blueprint = Blueprint("user", __name__)

# View all users
@users_blueprint.route("/users")
def users():
    users = user_repository.select_all()
    return render_template("/users", users=users)