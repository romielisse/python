-- Drop the tables if they already exist in order to start with a fresh
-- database. You will lose any movies you added.

DROP TABLE IF EXISTS Movie;
DROP TABLE IF EXISTS Category;

-- Create Movie and Category tables

CREATE TABLE Category (
    categoryID   INTEGER PRIMARY KEY     NOT NULL,
    name         TEXT                    NOT NULL
);

CREATE TABLE Movie(
    movieID     INTEGER PRIMARY KEY     NOT NULL,
    categoryID  INTEGER                 NOT NULL,
    name        TEXT                    NOT NULL,
    year        INTEGER                 NOT NULL,
    minutes     INTEGER                 NOT NULL,
    FOREIGN KEY(categoryID) REFERENCES Category(categoryID)
);

-- Populate the categories table

INSERT INTO Category VALUES (1, 'Animation');
INSERT INTO Category VALUES (2, 'Comedy');
INSERT INTO Category VALUES (3, 'History');

-- Populate the Movies table

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Spirit: Stallion of the Cimarron', 2002, 83, 1);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Spirited Away', 2001, 125, 1);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Aladdin', 1992, 90, 1);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Ice Age', 2002, 81, 1);
        
INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Toy Story', 1995, 81, 1);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Monty Python and the Holy Grail', 1975, 91, 2);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Monty Python''s Life of Brian', 1979, 94, 2);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Monty Python''s The Meaning of Life', 1983, 107, 2);
        
INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Gandhi', 1982, 191, 3);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Jinnah', 1998, 110, 3);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Lawrence of Arabia', 1962, 216, 3);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Hotel Rwanda', 2004, 121, 3);

INSERT INTO Movie (name, year, minutes, categoryID)
    VALUES ('Twelve Years a Slave', 2013, 134, 3);
