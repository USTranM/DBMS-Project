mysql <<EOFMYSQL
use sabburi;
show tables;

SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Player;

SET FOREIGN_KEY_CHECKS=1;

CREATE TABLE Team (
    TeamId INT AUTO_INCREMENT PRIMARY KEY,
    Location VARCHAR(255) NOT NULL,
    Nickname VARCHAR(255) NOT NULL,
    Conference VARCHAR(255) NOT NULL,
    Division VARCHAR(255) NOT NULL
);

CREATE TABLE Game (
    GameId INT AUTO_INCREMENT PRIMARY KEY,
    TeamId1 INT,
    TeamId2 INT,
    Score1 INT,
    Score2 INT,
    Date DATE,
    FOREIGN KEY (TeamId1) REFERENCES Team (TeamId),
    FOREIGN KEY (TeamId2) REFERENCES Team (TeamId)
);

CREATE TABLE Player (
    PlayerId INT AUTO_INCREMENT PRIMARY KEY,
    TeamId INT,
    Name VARCHAR(255) NOT NULL,
    Position VARCHAR(255) NOT NULL,
    FOREIGN KEY (TeamId) REFERENCES Team (TeamId)
);

-- INSERT INTO Team statement
INSERT INTO Team (Location, Nickname, Conference, Division) VALUES
('Manchester', 'United', 'Premier League', 'North'),
('Liverpool', 'Liverpool', 'Premier League', 'North'),
('Barcelona', 'FC Barcelona', 'La Liga', 'East'),
('Real Madrid', 'Real Madrid', 'La Liga', 'West');

INSERT INTO Game (TeamId1, TeamId2, Score1, Score2, Date) VALUES
(1, 2, 2, 1, '2024-04-15'),
(3, 4, 3, 2, '2024-04-17');

INSERT INTO Player (TeamId, Name, Position) VALUES
(1, 'Harry Kane', 'Forward'),
(1, 'Marcus Rashford', 'Midfielder'),
(2, 'Mohamed Salah', 'Forward'),
(2, 'Sadio Mané', 'Forward'),
(3, 'Lionel Messi', 'Forward'),
(3, 'Andres Iniesta', 'Midfielder'),
(4, 'Sergio Ramos', 'Defender'),
(4, 'Karim Benzema', 'Forward');

EOFMYSQL
