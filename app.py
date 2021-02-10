from flask import Flask, render_template

from controllers.festivals_controller import festivals_blueprint
from controllers.countries_controller import countries_blueprint
from controllers.users_controller import users_blueprint
# from controllers.attendees_controller import attendees_blueprint

app = Flask(__name__)

app.register_blueprint(festivals_blueprint)
app.register_blueprint(countries_blueprint)
app.register_blueprint(users_blueprint)
# app.register_blueprint(attendees_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)