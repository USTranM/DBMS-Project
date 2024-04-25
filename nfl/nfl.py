import sys
import traceback
import logging
import python_db


mysql_username = "mltran"  # please change to your username
mysql_password = "sei5aBei"  # please change to your MySQL password


def add_game(teamId1, teamId2, score1, score2, date):
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        res = python_db.executeSelect("SELECT * FROM Game;")
        res = res.split("\n")  # split the header and data for printing
        print(
            "<br/>"
            + "Table Game before:"
            + "<br/>"
            + res[0]
            + "<br/>"
            + res[1]
            + "<br/>"
        )
        for i in range(len(res) - 2):
            print(res[i + 2] + "<br/>")

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

        python_db.insert("Game", values)
        res = python_db.executeSelect("SELECT * FROM Game;")
        res = res.split("\n")  # split the header and data for printing
        print("<br/>" + "<br/>")
        print(
            "<br/>"
            + "Table ITEM after:"
            + "<br/>"
            + res[0]
            + "<br/>"
            + res[1]
            + "<br/>"
        )
        for i in range(len(res) - 2):
            print(res[i + 2] + "<br/>")
        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())

def view_players_position(position):
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        sql = "SELECT Player.Name, Player.Position, Team.Nickname FROM Player NATURAL JOIN Team WHERE Player.Position = %s;"
        res = python_db.executeSelect(sql, (position,))
        print("<table border='1'><tr><th>Name</th><th>Position</th><th>Team Nickname</th></tr>")
        for row in res:
            print(f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    
def view_all_teams():
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database

        sql = ("SELECT Team.Conference, Team.Location, Team.Nickname, "
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
        print("<table border='1'><tr><th>Team Nickname</th><th>Location</th><th>Conference</th></tr>")
        for row in res:
            print(f"<tr><td>{row['Nickname']}</td><td>{row['Location']}</td><td>{row['Conference']}</td></tr>")
        print("</table>")

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    
def view_team_games(team):
    html_table = "" 
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        
        sql = ("SELECT Team.Conference, Team.Location, Team.Nickname, "
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
               "ORDER BY Team.Conference ASC, Wins DESC, ConferenceWins DESC"
               "WHERE Team.Nickname = %s")

        res = python_db.executeSelect(sql, (team,))
        html_table = "<table border='1'><tr><th>Team Nickname</th><th>Location</th><th>Conference</th></tr>"
        for row in res:
            html_table += f"<tr><td>{row['Nickname']}</td><td>{row['Location']}</td><td>{row['Conference']}</td></tr>"
        html_table += "</table>"

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    
    return html_table

def view_games_date(date):
    html_table = "" 
    
    try:
        python_db.open_database(
            "localhost", mysql_username, mysql_password, mysql_username
        )  # open database
        
        sql = ('SELECT Team1.Location AS Team1Location, Team1.Nickname AS Team1Nickname, Team2.Location AS Team2Location, '
               'Team2.Nickname AS Team2Nickname, Game.Score1, Game.Score2,'
                'IF(Game.Score1 > Game.Score2, CONCAT(Team1.Location, ' ', Team1.Nickname),'
                'IF(Game.Score2 > Game.Score1, CONCAT(Team2.Location, ' ', Team2.Nickname), \'Draw\')) AS Winner'
                'FROM Game JOIN Team AS Team1 ON Game.TeamId1 = Team1.TeamId'
                'JOIN Team AS Team2 ON Game.TeamId2 = Team2.TeamId'
                'WHERE Game.Date = %s;')

        res = python_db.executeSelect(sql, (date,))
        html_table = "<table border='1'><tr><th>Home Nickname</th><th>Home Location</th><th>Opponent Team</th><th>Opponent Location</th></tr>"
        for row in res:
            html_table += f"<tr><td>{row['TeamNickname']}</td><td>{row['TeamLocation']}</td><td>{row['OpponentNickname']}</td><td>{row['OpponentLocation']}</td></tr>"
        html_table += "</table>"

        python_db.close_db()  # close db
    except Exception as e:
        logging.error(traceback.format_exc())
    
    return html_table


if __name__ == "__main__":

    if sys.argv[1] == 'add_game':
        teamId1, teamId2, score1, score2, date = sys.argv[2:]
        add_game(teamId1, teamId2, score1, score2, date)
    elif sys.argv[1] == 'new_player':
        print('Function not yet implemented.')
    elif sys.argv[1] == 'view_team':
        print('Function not yet implemented')
    elif sys.argv[1] == 'view_players_position':
        view_players_position(sys.argv[2])
    elif sys.argv[1] == 'view_all_teams':
        print('Function not yet implemented')
    elif sys.argv[1] == 'view_team_games':
        print('Function not yet implemented')
    elif sys.argv[1] == 'view_games_date':
        print('Function not yet implemented')
