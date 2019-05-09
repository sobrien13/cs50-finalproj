#!/usr/bin/python
#Handles all the database loading and interaction
#Handles all essential UI
import sqlite3
from World import *
from Battle import *
class Game:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
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
		
	def loadGame():
		filename = input("Loading game...\nEnter savefile name ex: 'example'\n")
		filename += ".db"
		connection = sqlite3.connect(filename)
	w = World()
	w.drawGrid()
	startMenu()
