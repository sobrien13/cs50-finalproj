#!/usr/bin/python
#Handles all the database loading and interaction
#Handles all essential UI
#Should import enemy and world code
import sqlite3
connection = sqlite3.connect("save.db")
c = connection.cursor()
c.execute("create table Character (name, strength, agi, intel)")
def startMenu():
	print("Py/Sqlite Text Based RPG.")
	print("1: New Game")
	print("2: Load Game")
	print("3: Exit")
	a = int(input("Choose one.\n"))
	while a > 3 or a < 1:
		print("Py/Sqlite Text Based RPG.")
		print("1: New Game")
		print("2: Load Game")
		print("3: Exit")
		a = int(input("Choose one.\n"))
	# if a == x do y
	if a == 1:
		startNewGame()
	elif a == 2:
		loadGame()
	else:
		exit()
def startNewGame():
	print("Starting new game...")
	initStats()
def loadGame():
	filename = input("Loading game...\nEnter savefile name ex: 'example'\n")
	filename += ".db"
	connection = sqlite3.connect(filename)
#Maybe good idea to move character creation to separate file?
#Is it possible to call Game.connection to reference the database?
#	Maybe just reference Game.c to directly access cursor not sure how that works
def initStats():
	#Writes character stats to save.db
	name = input("What is your name? ")
	pts = 15
	print("%s skill points remain.\n" % pts)
	strength = int(input("Enter %s\'s STRENGTH stat (1-10) \n" % name))
	pts -= strength
	print("%s skill points remain.\n" % pts)
	agi = int(input("Enter %s\'s AGILITY stat (1-10) \n" % name))
	pts -= agi
	print("%s skill points remain.\n" % pts)
	intel = int(input("Enter %s\'s INTELLIGENCE stat (1-10) \n" % name))
	pts -= intel
	print("%s skill points remain.\n" % pts)
	c.execute("insert into Character values(?, ?, ?, ?)", (name, strength, agi, intel))
def printStats():
	#Prints stats of all characters in save.db
	c.execute("select * from Character")
	rows = c.fetchall()
	for r in rows:
		print(r)
startMenu()

