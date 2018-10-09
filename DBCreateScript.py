# import mysql.connector
import psycopg2

# connect to local MySQL databases
#db = mysql.connector.connect(host="localhost", user="root", passwd="mysqlpasswd")
#cursor = db.cursor()

# connect to local PostgreSQL database
db = psycopg2.connect("host='localhost' dbname='snailRacing' user='root' password='psqlpass'")
cursor = db.cursor()

# script should only be run to initially set up the DB
# we want to delete ("drop") the DB if it already exists, as we can assume it's not needed
try:
    cursor.execute("DROP DATABASE snailRacing")
except:
    pass

# then need to create our snail racing DB
try:
    cursor.execute("CREATE DATABASE snailRacing")
except:
    pass

# db.commit() "saves" changes to the DB
db.commit()

# the connect statement from earlier essentially points to all local DBs that are present
# -- need to tell MySQL to use the snail racing DB specifically, with "USE"
cursor.execute("USE snailRacing")


# create user and user score tables
cursor.execute("CREATE TABLE users (userID INT AUTO_INCREMENT PRIMARY KEY,"
                                    "firstName VARCHAR(50),"
                                    "lastName VARCHAR(50),"
                                    "password VARCHAR(50),"
                                    "email VARCHAR(100))")

cursor.execute("CREATE TABLE userOverallScore (ID INT AUTO_INCREMENT PRIMARY KEY,"
                                                "userID INT,"
                                                "score INT,"
                                                "FOREIGN KEY(userID) REFERENCES users(userID))")


# create trainer and snails tables
cursor.execute("CREATE TABLE trainers (trainerID INT AUTO_INCREMENT PRIMARY KEY,"
                                        "name VARCHAR(50))")

cursor.execute("CREATE TABLE snails (snailID INT AUTO_INCREMENT PRIMARY KEY,"
                                    "trainerID INT,"
                                    "name VARCHAR(50),"
                                    "FOREIGN KEY(trainerID) REFERENCES trainers(trainerID))")


# create round and race tables
cursor.execute("CREATE TABLE round (roundID INT AUTO_INCREMENT PRIMARY KEY,"
                                    "prize VARCHAR(50),"
                                    "start DATETIME,"
                                    "finish DATETIME,"
                                    "roundName VARCHAR(20))")

cursor.execute("CREATE TABLE race (raceID INT AUTO_INCREMENT PRIMARY KEY,"
                                    "roundID INT,"
                                    "raceDate DATETIME,"
                                    "status INT,"
                                    "FOREIGN KEY(roundID) REFERENCES round(roundID))")


# create racecard, race predictions, and race result tables
cursor.execute("CREATE TABLE racecard (racecardID INT AUTO_INCREMENT PRIMARY KEY,"
                                        "raceID INT,"
                                        "snailID INT,"
                                        "FOREIGN KEY(raceID) REFERENCES race(raceID), "
                                        "FOREIGN KEY(snailID) REFERENCES snails(snailID))")


cursor.execute("CREATE TABLE raceResult (raceResultID INT AUTO_INCREMENT PRIMARY KEY,"
                                            "raceID INT,"
                                            "snailID INT,"
                                            "position INT,"
                                            "FOREIGN KEY(raceID) REFERENCES race(raceID),"
                                            "FOREIGN KEY(snailID) REFERENCES snails(snailID))")

cursor.execute("CREATE TABLE racePredictions (racePredID INT AUTO_INCREMENT PRIMARY KEY,"
                                            "raceID INT,"
                                            "userID INT,"
                                            "snailID INT,"
                                            "created DATETIME,"
                                            "FOREIGN KEY(raceID) REFERENCES race(raceID),"
                                            "FOREIGN KEY(userID) REFERENCES users(userID),"
                                            "FOREIGN KEY(snailID) REFERENCES snails(snailID))")

# create status tables
cursor.execute("CREATE TABLE status(statusID INT AUTO_INCREMENT PRIMARY KEY,"
                                    "status VARCHAR(50))")

# commit all changes to the DB
db.commit()

# close the DB connection once we're done
db.close()

