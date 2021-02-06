from flask import Flask, render_template, redirect, request, Blueprint
from models.user import User


users_blueprint = Blueprint("user", __name__)