--10.3 Database and Table 




-- drop test user if exists 
DROP USER IF EXISTS 'whatabook_user'@'localhost';


-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

/*
    insert store record 
*/
INSERT INTO store(locale)
    VALUES('1000 Galvin Rd S, Bellevue, NE 68005');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Two Towers', 'J.R.Tolkien', "The second part of The Lord of The Rings");

INSERT INTO book(book_name, author)
    VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien');

INSERT INTO book(book_name, author)
    VALUES('The Art of War', 'Sun Tzu');

INSERT INTO book(book_name, author)
    VALUES('Matterhorn', 'Karl Marlantes');

INSERT INTO book(book_name, author)
    VALUES('CyberWar', 'Richard Clarke');

INSERT INTO book(book_name, author)
    VALUES('THIS The Cyber Weapons Arms Race IS HOW THEY TELL ME THE WORLD ENDS', 'Nicole Perlroth');

INSERT INTO book(book_name, author)
    VALUES('With The Old Breed: At Peleliu and Okinawa', 'E.B Sledge');

/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Shaquille', 'Oatmeal');

INSERT INTO user(first_name, last_name)
    VALUES('Dirk', 'Diggler');

INSERT INTO user(first_name, last_name)
    VALUES('Gaylord', 'Focker');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Shaquille'), 
        (SELECT book_id FROM book WHERE book_name = 'With The Old Breed: At Peleliu and Okinawa')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Gaylord'),
        (SELECT book_id FROM book WHERE book_name = 'THIS The Cyber Weapons Arms Race IS HOW THEY TELL ME THE WORLD ENDS')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Dirk'),
        (SELECT book_id FROM book WHERE book_name = 'The Art of War')
    );

