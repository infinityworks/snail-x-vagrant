import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (roundID, prize, start, finish, roundName) VALUES (2, 100, '2018-10-16', '2018-10-21 00:00:00', 'Second Round'), (1, 100, '2018-10-22', '2018-10-26', 'First Round') ;")

# Adding trainers
cursor.execute("INSERT INTO trainers (trainerID, name) VALUES (1, 'Ash'), (2, 'Matt'), (3, 'James'), (4, 'Mike'), (5, 'Emily');")

# Creating snails in DB
cursor.execute("INSERT INTO snails (snailID, trainerID, name) VALUES (1, 1, 'Shelly Brooks'), (2, 2, 'Slime Shady'), (3, 3, 'Christian Snale'), (4, 4, 'Snail Platt'), (5, 5, 'Snailee Steinfeld');")

# Adding races
cursor.execute("INSERT INTO race (raceID, roundID, raceDate) VALUES (1, 1, '2018-10-18'), (2, 1, '2018-10-19'), (3, 1, '2018-10-20'), (4, 2, '2018-10-23'), (5, 2, '2018-10-24'), (6, 2, '2018-10-25');")

# Adding racecards
cursor.execute("INSERT INTO racecard (racecardID, raceID, snailID) VALUES (1, 1, 1), (2, 1, 2), (3, 1, 3), (4, 2, 1), (5, 2, 2), (6, 2, 3), (7, 6, 4), (8, 6, 2), (9, 6, 5), (10, 5, 5), (11, 5, 2), (12, 5, 3);")

    # commit all changes to the DB
db.commit()
#
# except:
#     print("Unable to insert DB tables.")

# close the DB connection once we're done
db.close()
