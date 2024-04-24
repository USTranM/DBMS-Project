import sys
import traceback
import logging
import python_db


mysql_username = "replaceIt"  # please change to your username
mysql_password = "replaceIt"  # please change to your MySQL password


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


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python3 add_game.py <TeamId1> <TeamId2> <Score1> <Score2> <Date>")
    else:
        teamId1, teamId2, score1, score2, date = sys.argv[1:]
        add_game(teamId1, teamId2, score1, score2, date)
