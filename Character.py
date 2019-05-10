#!/usr/bin/python
import sqlite3
#Handles all character database interaction
#
class Character:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
	def __init__(self):
		self.initTable()
		self.charId = self.getNewCharId()
		self.stats = self.getCurrent()
		print("Char ID:", self.charId)
	def initTable(self):
		self.c.execute("select count(name) from sqlite_master where type='table' and name='Character'")
		if self.c.fetchone()[0] == 1:
			print("Character table already exists.")
		else:
			print("Creating Character table.")
			self.c.execute("create table Character (id, name, strength, agi, hp, exp, gridRow, gridCol)")
	def isInTable(self):
		self.c.execute("select count(id) from Character")
		n = self.c.fetchone()[0]
		if n == 0:
			return False
		else:
			return True
	def getNewCharId(self):
		self.c.execute("select count(id) from Character")
		n = self.c.fetchone()[0]
		print(n+1)
		return n+1
	def initStats(self):
		self.exp = 0
		#Writes character stats to save.db
		self.name = input("What is your name? ")
		self.hp = 100
		pts = 10
		print("%s skill points remain.\n" % pts)
		self.strength = int(input("Enter %s\'s STRENGTH stat (1-10) \n" % self.name))
		pts -= self.strength
		print("%s skill points remain.\n" % pts)
		self.agi = int(input("Enter %s\'s AGILITY stat (1-10) \n" % self.name))
		pts -= self.agi
		self.c.execute("insert into Character (id, name, strength, agi, hp, exp) values(?, ?, ?, ?, ?, ?)", (self.charId, self.name, self.strength, self.agi, self.hp, self.exp))
		self.connection.commit()
	def savePosition(self, row, col):
		self.c.execute("update Character set gridRow = ? where id = ?", (row, self.charId))
		self.c.execute("update Character set gridCol = ? where id = ?", (col, self.charId))
		self.connection.commit()
	def printStats(self):
		#Prints stats of all characters in save.db
		self.c.execute("select * from Character")
		rows = self.c.fetchall()
		for r in rows:
			print(r[0], ")", "Name:", r[1], "STR:", r[2], "AGI:", r[3], "HP:", r[4], "R:", r[5], "C:", r[6], "EXP:", r[7])
	def deleteCurrentCharacter(self):
		self.c.execute("delete from Character where id = ?", (self.charId,))
		self.charId -= 1
		self.connection.commit()
	def addExp(self, exp):
		self.c.execute("update Character set exp = ? where id = ?", (exp, self.charId))
		self.connection.commit()
	def getCurrent(self):
		#Prints the current character's stats based on the charID
		#referenced using getCurrent['x'] syntax
		self.c.execute("select * from Character where id = ?", (self.charId,))
		rows = self.c.fetchall()
		CHAR_ID = 0
		CHAR_NAME = ""
		CHAR_STR = 0
		CHAR_AGI = 0
		CHAR_HP = 0
		CHAR_ROW = 0
		CHAR_COL = 0
		CHAR_EXP = 0
		for r in rows:
			CHAR_ID = r[0]
			CHAR_NAME = r[1]
			CHAR_STR = r[2]
			CHAR_AGI = r[3]
			CHAR_HP = r[4]
			CHAR_ROW = r[5]
			CHAR_COL = r[6]
			CHAR_EXP = r[7]
		stats = {
			"id" : CHAR_ID,
			"name" : CHAR_NAME,
			"stre" : CHAR_STR,
			"agi" : CHAR_AGI,
			"hp" : CHAR_HP,
			"row" : CHAR_ROW,
			"col" : CHAR_COL,
			"exp" : CHAR_EXP
		}
		return stats
	def numOfCharacters(self):
		self.c.execute("select count(id) from Character")
		n = self.c.fetchone()[0]
		return n