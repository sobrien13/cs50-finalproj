#!/usr/bin/python
#Establishes communication with Game.py
#Player position should probably be stored in 'save.db' and loaded through Game.py
#Evantual integration with enemy code to determine when/where battles begin
#Could store positions of enemy as integers row and col in 'save.db'
from Character import *
from Battle import *
class Map:
	ch = Character()
	b = Battle()
	def __init__(self):
		#instance variable grid
		#world initialized with saved playerdata
		self.grid = 	[["#", "~", "~", "#", "~"], 
			["#", "~", "~", "~", "~"], 
			["~", "~", "#", "~", "~"], 
			["~", "#", "~", "~", "#"], ]
		if self.ch.isInTable() == True:
			self.drawPlayer(self.ch.getCurrent()['row'], self.ch.getCurrent()['col'])
		else:
			self.drawPlayer(1, 2)
	def drawGrid(self):
		print("    0 1 2 3 4")
		rowNum = -1
		for r in self.grid:
			rowNum += 1
			print(rowNum, "|", r[0], r[1], r[2], r[3], r[4])
	def getPlayerPos(self):
		#Returns tuple which contains player position
		#Should return 1,2
		r = -1
		c = -1
		for row in self.grid:
			r += 1
			for col in row:
				c += 1
				if c == 5:
					c -= 5
				if col == "p":
					return r, c
	def isPlayerInWorld(self):
		r = -1
		c = -1
		for row in self.grid:
			r += 1
			for col in row:
				c += 1
				if c == 5:
					c -= 5
				if col == "p":
					return True
			return False
	def shouldSpawnEnemy(self):
		if self.isDangerous(self.getPlayerPos()[0], self.getPlayerPos()[1]) == False:
			self.b.startBattle()
	def isDangerous(self, inRow, inCol):
		if self.grid[inRow][inCol] == "#":
			return True
		else:
			return False
	def drawPlayer(self, r, c):
		self.grid[r][c] = "p"
	def movePlayer(self, byRow, byCol):
		row = self.getPlayerPos()[0]
		col = self.getPlayerPos()[1]
		self.grid[row][col] = "." # tiles already travelled notated with a .
		if row > 3 or col > 3:
			print("Can't move there.")
		else:
			self.grid[row+byRow][col+byCol] = "p"
	def movePlayerUp(self):
		self.movePlayer(-1,0)
	def movePlayerDown(self):
		self.movePlayer(1,0)
	def movePlayerRight(self):
		self.movePlayer(0,1)
	def movePlayerLeft(self):
		self.movePlayer(0,-1)	