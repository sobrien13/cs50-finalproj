#!/usr/bin/python
import sqlite3
connection = sqlite3.connect("save.db")
c = connection.cursor()
c.execute("create table Character (name, strength, agi, intel)")
def initStats():
	name = input("What is your name?")
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
	c.execute("select * from Character")
	rows = c.fetchall()
	for r in rows:
		print(r)
initStats()
printStats()
