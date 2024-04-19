mysql <<EOFMYSQL
use ;
show tables;

-- 1
INSERT INTO Game (TeamId1, TeamId2, Score1, Score2, Date) 
VALUES (1, 2, 3, 1, '2024-04-17');


-- 2
INSERT INTO Player (TeamId, Name, Position) 
VALUES (1, 'John Doe', 'Midfielder');


-- 3
SELECT * FROM Player WHERE TeamId = 1;


-- 4
SELECT * FROM Player WHERE Position = 'Forward';


-- 5
SELECT 
    Conference,
    Location,
    Nickname,
    COUNT(CASE WHEN Score1 > Score2 THEN 1 END) + COUNT(CASE WHEN Score1 < Score2 THEN 1 END) AS Wins
FROM 
    Team
LEFT JOIN 
    Game ON Team.TeamId IN (Game.TeamId1, Game.TeamId2)
GROUP BY 
    Conference, Location, Nickname
ORDER BY 
    Conference ASC, Wins DESC;


-- 6
SELECT 
    Team.Location AS TeamLocation,
    Team.Nickname AS TeamNickname,
    CONCAT(Opponent.Location, ' ', Opponent.Nickname) AS Opponent,
    Game.Date,
    CONCAT(Game.Score1, '-', Game.Score2) AS Score,
    IF(Game.TeamId1 = 1 AND Game.Score1 > Game.Score2 OR Game.TeamId2 = 1 AND Game.Score2 > Game.Score1, 'Won', 'Lost') AS Result
FROM 
    Game
JOIN 
    Team ON Game.TeamId1 = Team.TeamId OR Game.TeamId2 = Team.TeamId
JOIN 
    Team AS Opponent ON (Game.TeamId1 = Opponent.TeamId AND Game.TeamId2 != Opponent.TeamId)
                      OR (Game.TeamId2 = Opponent.TeamId AND Game.TeamId1 != Opponent.TeamId)
WHERE 
    Team.TeamId = 1;





-- 7
SELECT 
    Team1.Location AS Team1Location,
    Team1.Nickname AS Team1Nickname,
    Team2.Location AS Team2Location,
    Team2.Nickname AS Team2Nickname,
    Game.Score1,
    Game.Score2,
    IF(Game.Score1 > Game.Score2, CONCAT(Team1.Location, ' ', Team1.Nickname),
       IF(Game.Score2 > Game.Score1, CONCAT(Team2.Location, ' ', Team2.Nickname), 'Draw')) AS Winner
FROM 
    Game
JOIN 
    Team AS Team1 ON Game.TeamId1 = Team1.TeamId
JOIN 
    Team AS Team2 ON Game.TeamId2 = Team2.TeamId
WHERE 
    Game.Date = '2024-04-17';



EOFMYSQL