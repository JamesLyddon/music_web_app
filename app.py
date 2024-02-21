import os
from flask import Flask, request
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums')
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    all_albums = repository.all()
    albums_strings = [f"{album}" for album in all_albums]
    return '\n'.join(albums_strings)

@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form.get("title")
    release_year = int(request.form.get("release_year"))
    artist_id = int(request.form.get("artist_id"))
    album = {"title": title, "release_year": release_year, "artist_id": artist_id}
    repository.create(album)
    return ""

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

