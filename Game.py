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
	ch = Character()
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
		print("3: Main Menu")
		a = int(input("Choose one.\n"))
		while a > 3 or a < 1:
			print("1: View Map")
			print("2: Move")
			print("3: Main Menu")
			a = int(input("Choose one.\n"))
		if a == 1:
			self.viewMap()
		elif a == 2:
			self.moveMenu()
		elif a == 3:
			self.startMenu()
	def moveMenu(self):
		print("Move\n1: Up\n2: Down\n3: Right\n4: Left\n5: Exit Game")
		a = int(input("Choose one."))
		while a > 5 or a < 1:
			print("Move\n1: Up\n2: Down\n3: Right\n4: Left\n5: Exit Game")
			a = int(input("Choose one."))
		if a == 1:
			self.m.movePlayerUp()
			self.ch.savePosition(self.m.getPlayerPos()[0], self.m.getPlayerPos()[1])
		elif a == 2:
			self.m.movePlayerDown()
			self.ch.savePosition(self.m.getPlayerPos()[0], self.m.getPlayerPos()[1])
		elif a == 3:
			self.m.movePlayerRight()
			self.ch.savePosition(self.m.getPlayerPos()[0], self.m.getPlayerPos()[1])
		elif a == 4:
			self.m.movePlayerLeft()
			self.ch.savePosition(self.m.getPlayerPos()[0], self.m.getPlayerPos()[1])
		elif a == 5:
			exit()
	def viewMap(self):
		print("Your location in map:", self.m.getPlayerPos())
		self.m.drawGrid()
	def startNewGame(self):
		print("Starting new game...")
		self.ch.initStats()
	def loadGame(self):
		print("All characters currently in savefile:")
		self.ch.printStats()
		a = int(input("Choose one."))
		while a > self.ch.numOfCharacters() or a < 1:
			a = int(input("Choose one."))
		self.ch.charId = a