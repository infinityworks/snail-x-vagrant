import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (round_id, prize, start_date, closed, round_name) "
               "VALUES (2, 100, '2017-10-17', true , 'Second Round');")

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
               "VALUES (4, 2, '2017-10-18 12:00:00'), (5, 2, '2017-10-19 12:00:00'), (6, 2, '2017-10-20 12:00:00');")

# Adding racecards
cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
               "VALUES (1, 6, 1), (2, 6, 2), (3, 6, 3), "
               "       (7, 4, 2), (8, 4, 6), (9, 4, 5), "
               "        (4, 5, 4), (5, 5, 5), (6, 5, 1);")

#Adding results
cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position)"
               "VALUES (1, 6, 1, 2), (2, 6, 2, 1), (3, 6, 3, 3), "
               "       (7, 4, 2, 1), (8, 4, 6, 3), (9, 4, 5, 2), "
               "        (4, 5, 4, 2), (5, 5, 5, 1), (6, 5, 1, 3);")


# commit all changes to the DB
db.commit()


# close the DB connection once we're done
db.close()
