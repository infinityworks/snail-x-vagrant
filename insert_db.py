import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

try:
    # create user and user score tables
    cursor.execute("INSERT INTO round (roundID, prize, start, finish, roundName) VALUES (2, 100, '2018-10-15', '2018-10-30 00:00:00', 'Second Round'), (1, 100, '2018-10-20', '2018-10-25', 'First Round') ;")

    # Adding trainers
    cursor.execute("INSERT INTO trainers (trainerID, name) VALUES (1, 'Ash'), (2, 'Matt'), (3, 'James'), (4, 'Mike'), (5, 'Emily');")

    # Creating snails in DB
    cursor.execute("INSERT INTO snails (snailID, trainerID, name) VALUES (1, 1, 'Jerry'), (2, 2, 'Paul'), (3, 3, 'Gwen'), (4, 4, 'Barry'), (5, 5, 'Pam');")

    # Adding races
    cursor.execute("INSERT INTO race (raceID, roundID, raceDate) VALUES (1, 1, '2018-10-15'), (2, 1, '2018-10-15'), (3, 1, '2018-10-16'), (4, 1, '2018-10-17'), (5, 1, '2018-10-18'), (6, 2, '2018-10-21'), (7, 2, '2018-10-21'), (8, 2, '2018-10-22'),(9, 2, '2018-10-23'), (10, 2, '2018-10-29');")

    # Adding racecards
    cursor.execute("INSERT INTO racecard (racecardID, raceID, snailID) VALUES (1, 1, 1), (2, 1, 2), (3, 1, 3), (4, 1, 4), (5, 1, 5), (6, 2, 1), (7, 2, 2), (8, 2, 3), (9, 2, 4), (10, 2, 5);")

    # commit all changes to the DB
    db.commit()

except:
    print("Unable to insert DB tables.")

# close the DB connection once we're done
db.close()
