import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (round_id, prize, start_date, closed, round_name) "
               "VALUES (2, 100, '2018-10-17', false , 'Second Round');")

# Adding trainers
cursor.execute("INSERT INTO trainers (trainer_id, name) "
               "VALUES (1, 'Ash'), (2, 'Matt'), (3, 'James'), (4, 'Mike'), (5, 'Emily');")

# Creating snails in DB
cursor.execute("INSERT INTO snails (snail_id, trainer_id, name) "
               "VALUES (1, 1, 'Shelly Brooks'), (2, 2, 'Snail Platt'), "
               "(3, 3, 'Christian Snale'), (4, 4, 'Slime Shady'), (5, 5, 'Snailee Steinfeld'),"
               "(6, 2, 'Mi-shell Obama');")

# Adding races
cursor.execute("INSERT INTO race (race_id, round_id, race_date) "
               "VALUES (1, 2, '2018-10-18 12:00:00'), (2, 2, '2018-10-19 12:00:00'), (6, 2, '2019-10-20 12:00:00');")

# Adding racecards
cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
               "VALUES (1, 6, 1), (2, 6, 2), (3, 6, 3), "
               "       (7, 1, 2), (8, 1, 6), (9, 1, 5), "
               "        (4, 2, 4), (5, 2, 5), (6, 2, 1);")

# Adding raceresults
cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position) "
               "VALUES (1000, 6, 1, 1), (2000, 6, 2, 2), (3000, 6, 3, 3), "
               "       (7000, 1, 2, 3), (8000, 1, 6, 2), (9000, 1, 5, 1);")

# commit all changes to the DB
db.commit()


# close the DB connection once we're done
db.close()
