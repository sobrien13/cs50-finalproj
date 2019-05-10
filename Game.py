#!/usr/bin/python
#Handles all the database loading and interaction
#Handles all essential UI
import sqlite3
from Map import *
from Battle import *
from Character import *
class Game:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
	ch = Character(1)
	m = Map()
	def __init__(self):
		print("Py/Sqlite Text Based RPG.")
	def startMenu(self):
		print("1: New Game")
		print("2: Load Game")
		print("3: Exit")
		a = int(input("Choose one.\n"))
		while a > 3 or a < 1:
			print("1: New Game")
			print("2: Load Game")
			print("3: Exit")
			a = int(input("Choose one.\n"))
		# if a == x do y
		if a == 1:
			self.startNewGame()
		elif a == 2:
			self.loadGame()
		else:
			exit()
	def doMenu(self):
		print("What do you want to do?\n")
		print("1: View map")
		print("2: Move")
		print("3: Exit")
		a = int(input("Choose one.\n"))
		while a > 3 or a < 1:
			print("1: View Map")
			print("2: Move")
			print("3: Exit")
			a = int(input("Choose one.\n"))
		if a == 1:
			self.viewMap()
		elif a == 2:
			self.m.movePlayer()
		else:
			exit()
	def viewMap(self):
		print("Your location in map:", m.getPlayerPos())
		m.drawGrid()
	def startNewGame(self):
		print("Starting new game...")
		self.ch.createTable()
		self.ch.initStats()
	def loadGame():
		filename = input("Loading game...\nEnter savefile name ex: 'example'\n")
		filename += ".db"
		connection = sqlite3.connect(filename)
