"""
When I GET /albums
I get back a list of all albums
"""
def test_get_all_albums(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(1, Test Album 1, 2000, 5)\nAlbum(2, Test Album 2, 1995, 1)\nAlbum(3, Test Album 3, 2012, 3)\nAlbum(4, Test Album 4, 1989, 4)"

"""
when I POST /albums with the body parameters:
title=Voyage,release_year=2022, artist_id=2
I create a new album and add it to the table albums in the music database
and get back status code 200 and response None
"""
def test_create_new_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/albums", data={'title': 'Voyage', 'release_year': '2022', 'artist_id': '2'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""
    
    response = web_client.get("/albums")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Album(1, Test Album 1, 2000, 5)\nAlbum(2, Test Album 2, 1995, 1)\nAlbum(3, Test Album 3, 2012, 3)\nAlbum(4, Test Album 4, 1989, 4)\nAlbum(5, Voyage, 2022, 2)"

"""
When I GET /artists
I get back a list of all artists
"""
def test_get_all_artists(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist(1, Pixies, Punk)\nArtist(2, ABBA, Disco)\nArtist(3, Taylor Swift, Pop)\nArtist(4, Nina Simone, Jazz)"

"""
when I POST /artists with the body parameters:
name=Wild nothing, genre=Indie
I create a new artist and add it to the table artists in the music database
and get back status code 200 and response None
"""
def test_create_new_artist(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response = web_client.post("/artists", data={'name': 'Wild', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ""

    response = web_client.get("/artists")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Artist(1, Pixies, Punk)\nArtist(2, ABBA, Disco)\nArtist(3, Taylor Swift, Pop)\nArtist(4, Nina Simone, Jazz)\nArtist(5, Wild, Indie)"