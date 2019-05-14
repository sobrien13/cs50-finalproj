#!/usr/bin/env python3
#Handles all essential UI
# Main contributors:
# - Sean O'Brien
# - Alex Underwood
import sqlite3
from os import system
from Map import *
from Character import *
class Game:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
	ch = Character()
	m = Map()
	def __init__(self):
		print("Py/Sqlite Text Based RPG.")
	def start(self):
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
			system('clear')
			self.newGame()
		elif a == 2:
			system('clear')
			self.loadGame()
		else:
			exit()
	def doWhat(self):
		print("What do you want to do,", self.ch.getCurrent()['name'], "?\n")
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
			system('clear')
			self.viewMap()
		elif a == 2:
			system('clear')
			self.move()
		elif a == 3:
			system('clear')
			self.start()
	def move(self):
		print("Move\n1: Up\n2: Down\n3: Right\n4: Left\n5: Go Back")
		a = int(input("Choose one."))
		while a > 5 or a < 1:
			print("Move\n1: Up\n2: Down\n3: Right\n4: Left\n5: Go Back")
			a = int(input("Choose one."))
		if a == 1:
			self.m.movePlayerUp()
			self.update()
		elif a == 2:
			self.m.movePlayerDown()
			self.update()
		elif a == 3:
			self.m.movePlayerRight()
			self.update()
		elif a == 4:
			self.m.movePlayerLeft()
			self.update()
		elif a == 5:
			self.doWhat()
	def update(self):
		# unsure as to why the getPlayerPos() method is returning None
		self.ch.savePosition(self.m.getPlayerPos()[0], self.m.getPlayerPos()[1])
		self.m.shouldSpawnEnemy()
	def viewMap(self):
		print("Your location in map:", self.m.getPlayerPos())
		self.m.drawGrid()
	def newGame(self):
		print("Starting new game...")
		self.ch.initStats()
	def loadGame(self):
		print("All characters currently in savefile:\n0 ) Back to Main Menu")
		self.ch.printStats()
		a = int(input("Choose one."))
		while a > self.ch.numOfCharacters() or a < 0:
			a = int(input("Choose one."))
		if(a == 0):
			self.start()
		self.ch.charId = a
