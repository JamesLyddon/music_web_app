DROP TABLE IF EXISTS albums;

-- Then, we recreate them
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int,
    artist_id int
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 1', 2000, 5);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 2', 1995, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 3', 2012, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Test Album 4', 1989, 4);
