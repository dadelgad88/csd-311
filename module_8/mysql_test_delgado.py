
import mysql.connector
from mysql.connector import errorcode



config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);

-- INSTERT TEAM RECORDS
INSERT INTO team(team_name, mascot)
    VALUES("Night-Hawk", "Red the Hawk");
 
INSERT INTO team(team_name, mascot)
    VALUES('Dragon', 'Pete the Dragon');
    


SELECT team_id FROM team WHERE team_name = ('Night-Hawk')

SELECT team_id FROM team WHERE team_name = ('Dragon')


INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Shaquille', 'Oatmeal', (SELECT team_id FROM team WHERE team_name = 'Night-Hawk'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Gaylord', 'Focker', (SELECT team_id FROM team WHERE team_name = 'Night-Hawk'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Biggus', 'Dickus', (SELECT team_id FROM team WHERE team_name = 'Night-Hawk'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Dirk', 'Diggler', (SELECT team_id FROM team WHERE team_name = 'Dragon'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Mr', 'Pink', (SELECT team_id FROM team WHERE team_name = 'Dragon'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('McLovin', ' ', (SELECT team_id FROM team WHERE team_name = 'Dragon'));


