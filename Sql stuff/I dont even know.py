import sqlite3 as sql

scores = sql.connect('Scores.db')
cursor = scores.(cursor)
username = input('username:')

cursor.execute('CREATE TABLE players (name TEXT)')
scores.commit()
