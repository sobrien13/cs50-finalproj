#!/usr/bin/python
import sqlite3
from World import *
# * Creates Character(charId) class for evantually loading from database and creating new characters.
class Character:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
	def __init__(self, charId):
		self.charId = charId

	def createTable():
		c.execute("create table Character (id, name, strength, agi, hp, gridRow, gridCol)")
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
		c.execute("insert into Character values(?, ?, ?, ?)", (self.charId, name, strength, agi, hp))

	def savePosition():
		currentPos = world.getPlayerPos()
		row = currentPos[0]
		col = currentPos[1]
		c.execute("insert into Character (gridRow, col) values(?, ?)", (row, col))

	def printStats():
		#Prints stats of all characters in save.db
		c.execute("select * from Character")
		rows = c.fetchall()
		for r in rows:
			print(r)
