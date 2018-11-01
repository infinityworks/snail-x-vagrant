import psycopg2

db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()
try:
    # Adding users
    cursor.execute("INSERT INTO users (user_id, first_name, last_name, password, email)"
                "VALUES (1, 'Matt', 'Twomey', 'password', 'mtwomey@gmail.com'),"
                "        (2, 'James', 'Sheard', 'iluvmatt', 'jsheard@gmail.com'),"
                "        (3, 'Emily', 'Birch', 'carbsarelife', 'ebirch@gmail.com');")

    # Adding trainers
    cursor.execute("INSERT INTO trainers (trainer_id, name) "
                "VALUES (1, 'Ash'), (2, 'Matt'), (3, 'James'), (4, 'Mike'), (5, 'Emily');")

    # Creating snails in DB
    cursor.execute("INSERT INTO snails (snail_id, trainer_id, name) "
                "VALUES (1, 1, 'Shelly Brooks'), (2, 2, 'Snail Platt'), "
                "(3, 3, 'Christian Snale'), (4, 4, 'Slime Shady'), (5, 5, 'Snailee Steinfeld'),"
                "(6, 2, 'Mi-shell Obama');")

    # Create three closed rounds
    cursor.execute("INSERT INTO round (round_id, prize, start_date, closed, round_name) "
                "VALUES (1, 100, '2018-09-17', true , 'First Round'),"
                "(2, 100, '2018-09-19', true, 'Second Round'),"
                "(3, 100, '2018-09-21', true, 'Third Round');")

    # Races               
    cursor.execute("INSERT INTO race (race_id, round_id, race_date) "
                "VALUES (1, 1, '2018-10-18 12:00:00'), (2, 1, '2018-10-18 18:00:00'),"
                "(3, 2, '2018-10-19 12:00:00'), (4, 2, '2018-10-19 18:00:00'),"
                "(5, 3, '2018-10-21 12:00:00'), (6, 3, '2018-10-21 18:00:00');")

    # Adding racecards
    cursor.execute("INSERT INTO racecard (race_card_id, race_id, snail_id) "
                "VALUES (1, 1, 1), (2, 1, 2), (3, 1, 3), (4, 1, 4), "
                "(5, 2, 1), (6, 2, 2), (7, 2, 3), (8, 2, 4),"
                "(9, 3, 1), (10, 3, 2), (11, 3, 3), (12, 3, 4),"
                "(13, 4, 1), (14, 4, 2), (15, 4, 3), (16, 4, 4),"
                "(17, 5, 1), (18, 5, 2), (19, 5, 3), (20, 5, 4),"
                "(21, 6, 1), (22, 6, 2), (23, 6, 3), (24, 6, 4);")

    # Adding raceresults
    cursor.execute("INSERT INTO raceresult (race_result_id, race_id, snail_id, position) "
                "VALUES (1, 1, 1, 1), (2, 1, 2, 2), (3, 1, 3, 3), (4, 1, 4, 4), "
                "(5, 2, 1, 1), (6, 2, 2, 2), (7, 2, 3, 3), (8, 2, 4, 4),"
                "(9, 3, 1, 1), (10, 3, 2, 2), (11, 3, 3, 3), (12, 3, 4, 4),"
                "(13, 4, 1, 1), (14, 4, 2, 2), (15, 4, 3, 3), (16, 4, 4, 4),"
                "(17, 5, 1, 1), (18, 5, 2, 2), (19, 5, 3, 3), (20, 5, 4, 4),"
                "(21, 6, 1, 1), (22, 6, 2, 2), (23, 6, 3, 3), (24, 6, 4, 4);")

    # Adding racepredictions
    cursor.execute("INSERT INTO racepredictions (race_prediction_id, race_id, user_id, snail_id, created)"
                "VALUES (1, 1, 1, 1, '2018-10-18 00:00:00'), (2, 1, 2, 2, '2018-10-18 00:00:00'), (3, 1, 3, 3, '2018-10-18 00:00:00')," 
                "(4, 2, 1, 1, '2018-10-18 00:00:00'), (5, 2, 2, 2, '2018-10-18 00:00:00'), (6, 2, 3, 3, '2018-10-18 00:00:00'),"
                "(7, 3, 1, 1, '2018-10-18 00:00:00'), (8, 3, 2, 2, '2018-10-18 00:00:00'), (9, 3, 3, 3, '2018-10-18 00:00:00'),"
                "(10, 4, 1, 1, '2018-10-18 00:00:00'), (11, 4, 2, 2, '2018-10-18 00:00:00'), (12, 4, 3, 3, '2018-10-18 00:00:00'),"
                "(13, 5, 1, 1, '2018-10-18 00:00:00'), (14, 5, 2, 2, '2018-10-18 00:00:00'), (15, 5, 3, 3, '2018-10-18 00:00:00'),"
                "(16, 6, 1, 1, '2018-10-18 00:00:00'), (17, 6, 2, 2, '2018-10-18 00:00:00'), (18, 6, 3, 3, '2018-10-18 00:00:00');")

    # Add round results
    cursor.execute("INSERT INTO roundresult (round_result_id, user_id, round_id, score)"
                "VALUES (1, 1, 1, 10), (2, 1, 2, 10), (3, 1, 3, 10),"
                "(4, 2, 1, 6), (5, 2, 2, 6), (6, 2, 3, 6),"
                "(7, 3, 1, 2), (8, 3, 2, 2), (9, 3, 3, 2);")

    # commit all changes to the DB
    db.commit()
except:
    print("vroke")

# close the DB connection once we're done
db.close()