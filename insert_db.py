import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (round_id, prize, start_date, finish_date, round_name, status) "
               "VALUES (2, 100, '2018-10-22', '2018-11-30 00:00:00', 'Second Round', 'Scheduled'), "
               "        (1, 100, '2018-10-12', '2018-10-16', 'First Round', 'Closed') ;")

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
               "VALUES (1, 1, '2018-10-13 12:00:00'), (2, 1, '2018-10-14 12:00:00'), (3, 1, '2018-10-15 12:00:00'), "
               "(4, 2, '2018-11-12 12:00:00'), (5, 2, '2018-11-13 12:00:00'), (6, 2, '2018-11-14 12:00:00');")

# Adding racecards
cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
               "VALUES (1, 1, 1), (2, 1, 3), (3, 1, 5), "
               "       (4, 2, 2), (5, 2, 3), (6, 2, 4), "
               "        (7, 3, 3), (8, 3, 1), (9, 3, 4);")

cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position) "
               "VALUES (1, 1, 1, 1), (2, 1, 3, 2), (3, 1, 5, 3), (4, 2, 3, 1), (5, 2, 2, 2), (6, 2, 4, 3), "
               "        (7, 3, 1, 1), (8, 3, 4, 2), (9, 3, 2, 3)")
# commit all changes to the DB
db.commit()


# close the DB connection once we're done
db.close()
