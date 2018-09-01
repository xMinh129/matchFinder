from flask import Flask, flash, redirect, render_template, request, session, abort, url_for

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Then get the data from the form
        sport = request.form['sportsInput']

        location = request.form['locationInput']

        # Get the username/password associated with this tag
        # user, password = tag_lookup(tag)
        return {sport: sport, location: location}


@app.route("/rooms/<string:sport>/<string:location>/", methods=['GET'])
def rooms():
    sport = request.params.sport
    location = request.params.location
    rooms = []
    return {rooms: rooms}


# @app.route("/rooms/<string:sport>/<string:location>/")
# def rooms(sport, location):
#     return render_template(
#             'rooms.html', sport=sport, location=location)

if __name__ == "__main__":
    app.run()
