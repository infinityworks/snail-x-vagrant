# import mysql.connector
import psycopg2


try:
    db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
    cursor = db.cursor()

except:
    print("I am unable to connect to the database")



# create user and user score tables
cursor.execute("CREATE TABLE users (userID serial PRIMARY KEY,"
                                    "firstName VARCHAR(50),"
                                    "lastName VARCHAR(50),"
                                    "password VARCHAR(50),"
                                    "email VARCHAR(100));")

cursor.execute("CREATE TABLE userOverallScore (ID serial PRIMARY KEY,"
                                                "userID INT,"
                                                "score INT,"
                                                "FOREIGN KEY(userID) REFERENCES users(userID));")


# create trainer and snails tables
cursor.execute("CREATE TABLE trainers (trainerID serial PRIMARY KEY,"
                                        "name VARCHAR(50));")

cursor.execute("CREATE TABLE snails (snailID serial PRIMARY KEY,"
                                    "trainerID INT,"
                                    "name VARCHAR(50),"
                                    "FOREIGN KEY(trainerID) REFERENCES trainers(trainerID));")


# create round and race tables
cursor.execute("CREATE TABLE round (roundID serial PRIMARY KEY,"
                                    "prize VARCHAR(50),"
                                    "start TIMESTAMP,"
                                    "finish TIMESTAMP,"
                                    "roundName VARCHAR(20));")

cursor.execute("CREATE TABLE race (raceID serial PRIMARY KEY,"
                                    "roundID INT,"
                                    "raceDate TIMESTAMP,"
                                    "status INT,"
                                    "FOREIGN KEY(roundID) REFERENCES round(roundID));")


# create racecard, race predictions, and race result tables
cursor.execute("CREATE TABLE racecard (racecardID serial PRIMARY KEY,"
                                        "raceID INT,"
                                        "snailID INT,"
                                        "FOREIGN KEY(raceID) REFERENCES race(raceID), "
                                        "FOREIGN KEY(snailID) REFERENCES snails(snailID));")


cursor.execute("CREATE TABLE raceResult (raceResultID serial PRIMARY KEY,"
                                            "raceID INT,"
                                            "snailID INT,"
                                            "position INT,"
                                            "FOREIGN KEY(raceID) REFERENCES race(raceID),"
                                            "FOREIGN KEY(snailID) REFERENCES snails(snailID));")

cursor.execute("CREATE TABLE racePredictions (racePredID serial PRIMARY KEY,"
                                            "raceID INT,"
                                            "userID INT,"
                                            "snailID INT,"
                                            "created TIMESTAMP,"
                                            "FOREIGN KEY(raceID) REFERENCES race(raceID),"
                                            "FOREIGN KEY(userID) REFERENCES users(userID),"
                                            "FOREIGN KEY(snailID) REFERENCES snails(snailID));")

# create status tables
cursor.execute("CREATE TABLE status(statusID serial PRIMARY KEY,"
                                    "status VARCHAR(50));")

# commit all changes to the DB
db.commit()

# close the DB connection once we're done
db.close()

