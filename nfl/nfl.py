import sys
import traceback
import logging
import python_db
import numpy as np


mysql_username = "sabburi"  # please change to your username
mysql_password = "AChai5ch"  # please change to your MySQL password

#Problem 1
def add_game(teamId1, teamId2, score1, score2, date):
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        values = (
            "'"
            + teamId1
            + "','"
            + teamId2
            + "','"
            + score1
            + "','"
            + score2
            + "','"
            + date
            + "'"
        )
        column_names= "(TeamId1, TeamId2, Score1, Score2, Date)"
        python_db.insert("Game", column_names, values)
        print("Game added successfully!")
        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())


#Problem 2
def add_player(team, playerName, position):
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        values = (
            "'"
            + team
            + "','"
            + playerName
            + "','"
            + position
            + "'"
        )
        column_names= "(TeamId, Name, Position)"
        python_db.insert("Player", column_names, values)
        print("Player added successfully!")
        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

# Problem 3
def view_team(team):
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database

        sql = "SELECT * FROM Player WHERE TeamId = %s" 
        res = python_db.executeSelect(sql, (team,))
        print("<table border='1'><tr><th>Player ID</th><th>Team Id</th><th>Name</th><th>Position</th></tr>")
        for row in res:
            row = dict(zip(['PlayerId', 'TeamId', 'Name', 'Position'], row))
            print(f"<tr><td>{row['PlayerId']}</td><td>{row['TeamId']}</td><td>{row['Name']}</td><td>{row['Position']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

# Problem 4
def view_players_position(position):
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        sql = "SELECT Player.Name, Player.Position, Team.Nickname FROM Player NATURAL JOIN Team WHERE Player.Position = %s;"
        res = python_db.executeSelect(sql, (position,))
        print("<table border='1'><tr><th>Name</th><th>Position</th><th>Team Nickname</th></tr>")
        for row in res:
            row = dict(zip(['Name', 'Position', 'Nickname'], row))
            print(f"<tr><td>{row['Name']}</td><td>{row['Position']}</td><td>{row['Nickname']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    
# Problem 5
def view_all_teams():
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database

        sql = ("SELECT Team.Nickname, Team.Location, Team.Conference, "
               "COUNT(CASE WHEN Game.TeamId1 = Team.TeamId AND Score1 > Score2 THEN 1 "
               "            WHEN Game.TeamId2 = Team.TeamId AND Score2 > Score1 THEN 1 "
               "            ELSE NULL END) AS Wins, "
               "COUNT(CASE WHEN OpponentTeam.Conference = Team.Conference "
               "               AND ((Game.TeamId1 = Team.TeamId AND Score1 > Score2) "
               "                    OR (Game.TeamId2 = Team.TeamId AND Score2 > Score1)) "
               "           THEN 1 ELSE NULL END) AS ConferenceWins "
               "FROM Team "
               "LEFT JOIN Game ON Team.TeamId IN (Game.TeamId1, Game.TeamId2) "
               "LEFT JOIN Team AS OpponentTeam ON (Game.TeamId1 = OpponentTeam.TeamId OR Game.TeamId2 = OpponentTeam.TeamId) "
               "GROUP BY Team.Conference, Team.Location, Team.Nickname "
               "ORDER BY Team.Conference ASC, Wins DESC, ConferenceWins DESC")

        res = python_db.executeSelect(sql)
        print("<table border='1'><tr><th>Team Nickname</th><th>Location</th><th>Conference</th><th>Total Wins</th><th>Wins During Conference</th></tr>")
        for row in res:
            row = dict(zip(['TeamNickname', 'TeamLocation', 'TeamConference', 'Wins', 'ConferenceWins'], row))
            print(f"<tr><td>{row['TeamNickname']}</td><td>{row['TeamLocation']}</td><td>{row['TeamConference']}</td><td>{row['Wins']}</td><td>{row['ConferenceWins']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

# Problem 6
def view_team_games(team):
    html_table = "" 
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        
        sql = ("SELECT Team.Nickname AS TeamNickname, Team.Location AS TeamLocation, Opponent.Nickname AS OpponentNickname, "
            "Opponent.Location AS OpponentLocation, Game.Date, Game.Score1, Game.Score2, "
            "IF(Game.TeamId1 = 1 AND Game.Score1 > Game.Score2, 'Won', 'Lost') AS Result "
            "FROM Game "
            "JOIN Team ON Game.TeamId1 = Team.TeamId OR Game.TeamId2 = Team.TeamId "
            "JOIN (SELECT TeamId, Location, Nickname FROM Team) AS Opponent ON Game.TeamId1 = Opponent.TeamId OR Game.TeamId2 = Opponent.TeamId "
            "WHERE Team.Nickname = %s")

        res = python_db.executeSelect(sql, (team,))
        print(f"<table border='1'><tr><th>Team Nickname</th><th>Team Location</th><th>Opponent Nickname</th><th>Team Location</th><th>Game Date</th><th>Team Score</th><th>Opponent Score</th><th>Did {team} win?</th></tr>")
        for row in res:
            row = dict(zip(['TeamNickname', 'TeamLocation', 'OpponentNickname', 'OpponentLocation', 'Date', 'Score1', 'Score2', 'WL'], row))
            print(f"<tr><td>{row['TeamNickname']}</td><td>{row['TeamLocation']}</td><td>{row['OpponentNickname']}</td><td>{row['OpponentLocation']}</td><td>{row['Date']}</td><td>{row['Score1']}</td><td>{row['Score2']}</td><td>{row['WL']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

# Problem 7
def view_games_date(date):
    html_table = "" 
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        
        sql = (
            "SELECT Team1.Nickname AS Team1Nickname, Team1.Location AS Team1Location, Team2.Nickname AS Team2Nickname, "
            "Team2.Location AS Team2Location, Game.Score1, Game.Score2, "
            "IF(Game.Score1 > Game.Score2, CONCAT(Team1.Location, ' ', Team1.Nickname), "
            "IF(Game.Score2 > Game.Score1, CONCAT(Team2.Location, ' ', Team2.Nickname), 'Draw')) AS Winner "
            "FROM Game "
            "JOIN Team AS Team1 ON Game.TeamId1 = Team1.TeamId "
            "JOIN Team AS Team2 ON Game.TeamId2 = Team2.TeamId "
            "WHERE Game.Date = %s;"
        )

        res = python_db.executeSelect(sql, (date,))
        print("<table border='1'><tr><th>Team 1 Nickname</th><th>Team 1 Location</th><th>Team 2 Nickname</th><th>Team 2 Location</th><th>Team 1 Score</th><th>Team 2 Score</th><th>Winner</th></tr>")
        for row in res:
            row = dict(zip(['Team1Nickname', 'Team1Location', 'Team2Nickname', 'Team2Location', 'Score1', 'Score2', 'WL'], row))
            print(f"<tr><td>{row['Team1Nickname']}</td><td>{row['Team1Location']}</td><td>{row['Team2Nickname']}</td><td>{row['Team2Location']}</td><td>{row['Score1']}</td><td>{row['Score2']}</td><td>{row['WL']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

# Bonus Query
def view_best_division():

    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        sql = ("SELECT p.Name, p.Position, t.Nickname, t.Division"
                "FROM Player p JOIN Team t ON p.TeamId = t.TeamId"
                "JOIN (SELECT t.Division FROM Team t JOIN Game g ON t.TeamId = g.TeamId1 OR t.TeamId = g.TeamId2"
                "WHERE (g.TeamId1 = t.TeamId AND g.Score1 > g.Score2) OR (g.TeamId2 = t.TeamId AND g.Score2 > g.Score1)"
                "GROUP BY t.Division ORDER BY COUNT(*) DESC LIMIT 1) best_division ON t.Division = best_division.Division;")
        res = python_db.executeSelect(sql)
        print("<table border='1'><tr><th>Player Name</th><th>Player Position</th><th>Team Nickname</th><th>Team Division</th></tr>")
        for row in res:
            row = dict(zip(['Name', 'Position', 'Nickname', 'Division'], row))
            print(f"<tr><td>{row['Name']}</td><td>{row['Position']}</td><td><strong class=\"text-white\">{row['Nickname']}</strong></td><td>{row['Division']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    

if __name__ == "__main__":

    if mysql_username == '':
        print('Change the username/password!')

    if sys.argv[1] == 'index':
        view_best_division()
    elif sys.argv[1] == 'add_game':
        teamId1, teamId2, score1, score2, date = sys.argv[2:]
        add_game(teamId1, teamId2, score1, score2, date)
    elif sys.argv[1] == 'add_player':
        team, playerName, position = sys.argv[2:]
        add_player(team, playerName, position)
    elif sys.argv[1] == 'view_team':
        team= sys.argv[2]
        view_team(team)
    elif sys.argv[1] == 'view_players_position':
        view_players_position(sys.argv[2])
    elif sys.argv[1] == 'view_all_teams':
        view_all_teams()
    elif sys.argv[1] == 'view_team_games':
        view_team_games(sys.argv[2])
    elif sys.argv[1] == 'view_games_date':
        view_games_date(sys.argv[2])
