mysql <<EOFMYSQL
use mltran;
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
    Team.Conference,
    Team.Location,
    Team.Nickname,
    COUNT(CASE
            WHEN Game.TeamId1 = Team.TeamId AND Score1 > Score2 THEN 1  -- Team is TeamId1 and won
            WHEN Game.TeamId2 = Team.TeamId AND Score2 > Score1 THEN 1  -- Team is TeamId2 and won
            ELSE NULL
          END) AS Wins,
    COUNT(CASE
            WHEN OpponentTeam.Conference = Team.Conference
                AND ((Game.TeamId1 = Team.TeamId AND Score1 > Score2)
                    OR (Game.TeamId2 = Team.TeamId AND Score2 > Score1)) THEN 1
            ELSE NULL  -- Count only wins within the same conference
          END) AS ConferenceWins
FROM
    Team
LEFT JOIN
    Game ON Team.TeamId IN (Game.TeamId1, Game.TeamId2)
LEFT JOIN
    Team AS OpponentTeam ON (Game.TeamId1 = OpponentTeam.TeamId OR Game.TeamId2 = OpponentTeam.TeamId)
GROUP BY
    Team.Conference, Team.Location, Team.Nickname
ORDER BY
    Team.Conference ASC, Wins DESC, ConferenceWins DESC;



-- 6
SELECT 
    Team.Location AS TeamLocation,
    Team.Nickname AS TeamNickname,
    Opponent.Location AS OpponentLocation,
    Opponent.Nickname AS OpponentNickname,
    Game.Date,
    Game.Score1,
    Game.Score2,
    IF(Game.TeamId1 = 1 AND Game.Score1 > Game.Score2, 'Won', 'Lost') AS Result
FROM 
    Game
JOIN 
    Team ON Game.TeamId1 = Team.TeamId OR Game.TeamId2 = Team.TeamId
JOIN 
    (
        SELECT 
            TeamId, Location, Nickname 
        FROM 
            Team
    ) AS Opponent ON Game.TeamId1 = Opponent.TeamId OR Game.TeamId2 = Opponent.TeamId;


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

-- 8
SELECT p.Name, p.Position, t.Nickname, t.Division
FROM Player p
JOIN Team t ON p.TeamId = t.TeamId
JOIN (
    SELECT t.Division
    FROM Team t
    JOIN Game g ON t.TeamId = g.TeamId1 OR t.TeamId = g.TeamId2
    WHERE (g.TeamId1 = t.TeamId AND g.Score1 > g.Score2) OR (g.TeamId2 = t.TeamId AND g.Score2 > g.Score1)
    GROUP BY t.Division
    ORDER BY COUNT(*) DESC
    LIMIT 1
) best_division ON t.Division = best_division.Division;


EOFMYSQL
