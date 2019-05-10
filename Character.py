#!/usr/bin/python
import sqlite3
from Map import *
# * Creates Character(charId) class for evantually loading from database and creating new characters.
class Character:
	connection = sqlite3.connect("save.db")
	c = connection.cursor()
	m = Map()
	def __init__(self):
		self.initTable()
		self.charId = self.getNewCharId()
		print("Char ID:", self.charId)
	def initTable(self):
		self.c.execute("select count(name) from sqlite_master where type='table' and name='Character'")
		if self.c.fetchone()[0] == 1:
			print("Character table already exists.")
		else:
			print("Creating Character table.")
			self.c.execute("create table Character (id, name, strength, agi, hp, gridRow, gridCol)")
	def getNewCharId(self):
		self.c.execute("select count(id) from Character")
		n = self.c.fetchone()[0]
		print(n+1)
		return n+1
	def initStats(self):
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
		self.c.execute("insert into Character (id, name, strength, agi, hp) values(?, ?, ?, ?, ?)", (self.charId, self.name, self.strength, self.agi, self.hp))
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
			print(r[0], ")", "Name:", r[1], "STR:", r[2], "AGI:", r[3], "HP:", r[4], "R:", r[5], "C:", r[6])
	def numOfCharacters(self):
		self.c.execute("select count(id) from Character")
		n = self.c.fetchone()[0]
		return n