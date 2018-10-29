import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (round_id, prize, start_date, closed, round_name) "
               "VALUES (1, 100, '2018-10-17', false , 'Second Round');")

# Adding trainers
cursor.execute("INSERT INTO trainers (trainer_id, name) "
               "VALUES (1, 'Ash'), (2, 'Matt'), (3, 'James'), (4, 'Mike'), (5, 'Emily');")

# Creating snails in DB
cursor.execute("INSERT INTO snails (snail_id, trainer_id, name) "
               "VALUES (1, 1, 'Shelly Brooks'), (2, 2, 'Snail Platt'), "
               "(3, 3, 'Christian Snale'), (4, 4, 'Slime Shady'), (5, 5, 'Snailee Steinfeld'),"
               "(6, 2, 'Mi-shell Obama');")

# Adding races (2 races  that occurred in the past, one of which has a sresult recorded for it. The test result json
# data provides the result for race 2, and the round is then changed to closed.
cursor.execute("INSERT INTO race (race_id, round_id, race_date) "
               "VALUES (1, 1, '2018-10-18 12:00:00'), (2, 1, '2018-10-19 12:00:00');")

# Adding racecards
cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
               "VALUES (7, 1, 2), (8, 1, 6), (9, 1, 5), "
               "        (4, 2, 4), (5, 2, 5), (6, 2, 1);")

# Adding raceresults
cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position) "
               "VALUES (1000, 1, 4, 4), (2000, 1, 3, 3), (3000, 1, 2, 2), (4000, 1, 2, 2), (5000, 1, 1, 1);")

# commit all changes to the DB
db.commit()


# close the DB connection once we're done
db.close()
