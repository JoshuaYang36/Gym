import sqlite3 as lite
import sys
import os


def main():

    # Setting new DB (week) if it does not exist


    week = raw_input("Enter the week you are in: ").lower()             # Need to add input check and fix

    file_path = week + ".db"
    path = "/Users/Josh/Desktop/" + file_path

    if os.path.isfile(path):
        print("hello")
        con = lite.connect(file_path)
        cur = con.cursor() 
    else:
        con = lite.connect(file_path)
        with con:
    
            cur = con.cursor()    
            cur.execute("CREATE TABLE Workouts(Name TEXT, Weight INT, Sets INT, Repetition INT)")

    # Entering user input into DB
    name = raw_input("Enter name of your exercise: ")
    weight = raw_input("Enter weight used: ")
    sets = raw_input("Enter number of sets: ")
    reps = raw_input("Enter repetitions: ")

    cur.execute("INSERT INTO Workouts (Name, Weight, Sets, Repetition) VALUES (?,?,?,?)", (name, weight, sets, reps))

    con.commit()

    cur.execute("SELECT * FROM Workouts")
    print(cur.fetchall())


if __name__ == '__main__':
    main()

        