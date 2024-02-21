"""
when I POST /albums with the body parameters:
title=Voyage
release_year=2022
artist_id=2
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
