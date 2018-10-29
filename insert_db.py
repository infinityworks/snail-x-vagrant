import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# create user and user score tables
cursor.execute("INSERT INTO round (round_id, prize, start_date, closed, round_name) "
               "VALUES (2, 100, '2018-10-10', true , 'First Round'),"
               "        (1, 100, '2018-10-20', false , 'Second Round'),"
               "        (3, 100, '2018-09-04', true, 'Third Round'),"
               "        (4, 100, '2018-11-03', false, 'Fourth Round');")

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
               "VALUES (1, 1, '2018-10-21 12:00:00'), (2, 1, '2018-10-23 12:00:00'), (3, 1, '2018-10-24 10:00:00'), "
               "        (4, 1, '2018-10-25 12:00:00'), (5, 1, '2018-10-26 12:00:00'), (6, 1, '2018-10-27 12:00:00'),"
               "        (7, 2, '2018-10-11 12:00:00'), (8, 2, '2018-10-12 12:00:00'), (9, 2, '2018-10-13 10:00:00'), "
               "        (10, 2, '2018-10-14 12:00:00'), (11, 2, '2018-10-15 12:00:00'), (12, 2, '2018-10-16 12:00:00'),"
               "        (13, 3, '2018-09-05 12:00:000'), (14, 3, '2018-09-06 12:00:00'), (15, 3, '2018-10-07 12:00:00'),"
               "        (16, 4, '2018-11-04 12:00:000'), (17, 4, '2018-11-05 12:00:00'), (18, 4, '2018-11-07 12:00:00');")

# Adding racecards
cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
               "VALUES (1, 1, 1), (2, 1, 2), (3, 1, 3), "
               "        (4, 2, 2), (5, 2, 6), (6, 2, 5), "
               "        (7, 3, 4), (8, 3, 5), (9, 3, 1),"
               "        (10, 4, 1), (11, 4, 2), (12, 4, 3), "
               "        (13, 5, 2), (14, 5, 6), (15, 5, 5), "
               "        (16, 6, 4), (17, 6, 5), (18, 6, 1),"
               "        "
               "        (19, 7, 1), (20, 7, 2), (21, 7, 3), "
               "        (22, 8, 2), (23, 8, 6), (24, 8, 5), "
               "        (25, 9, 4), (26, 9, 5), (27, 9, 1),"
               "        (28, 10, 1), (29, 10, 2), (30, 10, 3), "
               "        (31, 11, 2), (32, 11, 6), (33, 11, 5), "
               "        (34, 12, 4), (35, 12, 5), (36, 12, 1),"
               ""
               "        (37, 13, 4), (38, 13, 2), (39, 13, 6),"
               "        (40, 14, 1), (41, 14, 2), (42, 14, 5),"
               "        (43, 15, 5), (44, 15, 1), (45, 15, 3),"
               "        "
               "        (46, 16, 5), (47, 16, 2), (48, 16, 1),"
               "        (49, 17, 6), (50, 17, 4), (51, 17, 3),"
               "        (52, 18, 5), (53, 18, 1), (54, 18, 3);")

cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position) "
               "VALUES (1, 1, 1, 2), (2, 1, 2, 1), (3, 1, 3, 3), "
               "        (4, 2, 2, 3), (5, 2, 6, 2), (6, 2, 5, 1), "
               "        (7, 3, 4, 1), (8, 3, 5, 2), (9, 3, 1, 3),"
               "       "
               "        (10, 7, 1, 2), (11, 7, 2, 1), (12, 7, 3, 3), "
               "        (13, 8, 2, 3), (14, 8, 6, 2), (15, 8, 5, 1), "
               "        (16, 9, 4, 1), (17, 9, 5, 2), (18, 9, 1, 3),"
               "        (19, 10, 1, 2), (20, 10, 2, 1), (21, 10, 3, 3), "
               "        (22, 11, 2, 3), (23, 11, 6, 2), (24, 11, 5, 1), "
               "        (25, 12, 4, 1), (26, 12, 5, 2), (27, 12, 1, 3),"
               ""
               "        (28, 13, 4, 1), (29, 13, 2, 2), (30, 13, 6, 3),"
               "        (31, 14, 1, 3), (32, 14, 2, 2), (33, 14, 5, 1),"
               "        (34, 15, 5, 2), (35, 15, 1, 3), (36, 15, 3, 1);")

# commit all changes to the DB
db.commit()


# close the DB connection once we're done
db.close()
