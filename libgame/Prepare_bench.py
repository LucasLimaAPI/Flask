import mysql.connector
from mysql.connector import errorcode

print("Connecting")
try:
    conn = mysql.connector.connect(
        host='10.204.38.32',
        port=3306,  # Porta padrão do MySQL
        user='root',
        password='Lucas110502'
    )
    print("Connected successfully!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is going wrong with your username or password")
    else:
        print(err)


cursor = conn.cursor()

cursor.execute('DROP DATABASE IF EXISTS `libgame`')

cursor.execute('CREATE DATABASE `libgame`')

cursor.execute('use `libgame`')

#Creating tables

TABLES = {}
TABLES ['Games'] = ('''
        CREATE TABLE `games`( `id` int(11) NOT NULL AUTO_INCREMENT,
        `name` varchar(50) NOT NULL,
        `category` varchar(40) NOT NULL,
        `console` varchar(20) NOT NULL, 
        PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET= utf8 COLLATE=utf8_bin;''')

TABLES['Usernames'] = ('''
        CREATE TABLE `usernames`(
        `nome` varchar(20) NOT NULL,
        `nickname` varchar(8) NOT NULL,
        `password` varchar(100) NOT NULL,
        PRIMARY KEY (`nickname`)
        ) ENGINE=InnoDB DEFAULT CHARSET= utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
  table_sql = TABLES[table_name]
  try:
    print('Creating table {}'.format(table_name), end= ' ')
    cursor.execute(table_sql)
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
      print('Already exists')
    else:
      print(err.msg)
  else:
    print('OK')

# Inserting users

username_sql = 'INSERT INTO usersnames (nm, nickname, password) VALUES (%s,%s,%s)'
usernames = [
  ("Lucas Lima", "BD", "Lucas110502"),
  ("Kaline Fernanda", "Mila", "300521"),
  ("Luka Salima", "LK", "110223")
]

cursor.executemany(username_sql, usernames)

cursor.execute('select * from libgame.usernames')
print('-------------------Users--------------------')
for user in cursor.fetchall():
  print(user[1])

# Inserting games
games_sql = 'INSERT INTO games (name, category, console) VALUES (%s,%s,%s)'
games = [
 ('Darksiders', 'Action', 'Mult-platform'),
 ('Phamosphobia', 'Horror', 'Computer'),
 ('Skyrim', 'RPG', 'Mult-platform'),
 ('Mortal Kombat', 'Fight', 'PS2'),
 ('Celeste', 'Puzzle', 'PC'),
 ('League Of Legends', 'Moba','PC'),
]
cursor.executemany(games_sql,games)

cursor.execute('select * from libgame.games ')
print('-------------------Games--------------------')
for game in cursor.fetchall():
  print(game[1])









