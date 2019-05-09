#!/usr/bin/python
import sqlite3
import Game
from World import *
#Handles all character related definitions
class Character:
	connection = Game.connection
	c = connection.cursor()
	createTable = c.execute("create table Character (name, strength, agi, intel, hp, rowInGrid, colInGrid)")
	world = World()
	def initStats():
		#Writes character stats to save.db
		name = input("What is your name? ")
		hp = 100
		pts = 10
		print("%s skill points remain.\n" % pts)
		strength = int(input("Enter %s\'s STRENGTH stat (1-10) \n" % name))
		pts -= strength
		print("%s skill points remain.\n" % pts)
		agi = int(input("Enter %s\'s AGILITY stat (1-10) \n" % name))
		pts -= agi
		c.execute("insert into Character values(?, ?, ?, ?)", (name, strength, agi, hp))
	def savePosition():
		currentPos = world.getPlayerPos()
		row = currentPos[0]
		col = currentPos[1]
		c.execute("insert into Character(rowInGrid, colInGrid)", (row, col))
	def printStats():
		#Prints stats of all characters in save.db
		c.execute("select * from Character")
		rows = c.fetchall()
		for r in rows:
			print(r)