# import mysql.connector
import psycopg2



db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

try:

    # create user and user score tables
    cursor.execute("CREATE TABLE users (user_id serial PRIMARY KEY,"
                                        "first_name VARCHAR(50),"
                                        "last_name VARCHAR(50),"
                                        "password VARCHAR(255),"
                                        "email VARCHAR(100));")

    cursor.execute("CREATE TABLE userOverallScore (user_overall_score_id serial PRIMARY KEY,"
                                                    "user_id INT,"
                                                    "score INT,"
                                                    "FOREIGN KEY(user_id) REFERENCES users(user_id));")


    # create trainer and snails tables
    cursor.execute("CREATE TABLE trainers (trainer_id serial PRIMARY KEY,"
                                            "name VARCHAR(50));")

    cursor.execute("CREATE TABLE snails (snail_id serial PRIMARY KEY,"
                                        "trainer_id INT,"
                                        "name VARCHAR(50),"
                                        "FOREIGN KEY(trainer_id) REFERENCES trainers(trainer_id));")


    # create round and race tables
    cursor.execute("CREATE TABLE round (round_id serial PRIMARY KEY,"
                                        "prize VARCHAR(50),"
                                        "start_date TIMESTAMP,"
                                        "closed BOOLEAN,"
                                        "round_name VARCHAR(20));")

    cursor.execute("CREATE TABLE race (race_id serial PRIMARY KEY,"
                                        "round_id INT,"
                                        "status VARCHAR(20),"
                                        "race_date TIMESTAMP,"
                                        "FOREIGN KEY(round_id) REFERENCES round(round_id));")


    # create racecard, race predictions, and race result tables
    cursor.execute("CREATE TABLE racecard (race_card_id serial PRIMARY KEY,"
                                            "race_id INT,"
                                            "snail_id INT,"
                                            "FOREIGN KEY(race_id) REFERENCES race(race_id), "
                                            "FOREIGN KEY(snail_id) REFERENCES snails(snail_id));")

    cursor.execute("CREATE TABLE raceResult (race_result_id serial PRIMARY KEY,"
                                                "race_id INT,"
                                                "snail_id INT,"
                                                "position INT,"
                                                "FOREIGN KEY(race_id) REFERENCES race(race_id),"
                                                "FOREIGN KEY(snail_id) REFERENCES snails(snail_id));")

    cursor.execute("CREATE TABLE racePredictions (race_prediction_id serial PRIMARY KEY,"
                                                "race_id INT,"
                                                "user_id INT,"
                                                "snail_id INT,"
                                                "created TIMESTAMP,"
                                                "FOREIGN KEY(snail_id) REFERENCES snails(snail_id),"
                                                "FOREIGN KEY(user_id) REFERENCES users(user_id),"
                                                "FOREIGN KEY(race_id) REFERENCES race(race_id))")

    cursor.execute("CREATE VIEW fullDataView AS SELECT "
                   "        round.round_id,   "
                   "        round.round_name, "
                   "        round.start_date, "
                   "        round.closed, "
                   "        racecard.race_id, "
                   "        race.race_date, "
                   "        snails.name AS snail_name, "
                   "        trainers.name AS trainer_name, "
                   "        raceresult.position "
                   "    FROM racecard "
                   "    JOIN snails ON racecard.snail_id = snails.snail_id "
                   "    JOIN trainers ON snails.trainer_id = trainers.trainer_id "
                   "    JOIN race ON race.race_id = racecard.race_id "
                   "    JOIN round ON round.round_id = race.round_id "
                   "    JOIN raceresult ON racecard.race_id = raceresult.race_id "
                   "                    AND snails.snail_id = raceresult.snail_id;")

    # commit all changes to the DB
    db.commit()
except:
    print("I am unable to connect to the database")

# close the DB connection once we're done
db.close()
