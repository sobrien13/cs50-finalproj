#!/usr/bin/python
#Establishes communication with Game.py
#Player position should probably be stored in 'save.db' and loaded through Game.py
#Evantual integration with enemy code to determine when/where battles begin
#Could store positions of enemy as integers row and col in 'save.db'
class World:
	def __init__(self, playerAtRow=1, playerAtCol=2):
		#instance variable grid
		#world initialized with saved playerdata
		self.grid = 	[["~", "~", "~", "~", "~"], 
			["~", "~", "~", "~", "~"], 
			["~", "~", "~", "~", "~"], 
			["~", "~", "~", "~", "~"], ]
		while isPlayerInWorld() != True:
			drawPlayer(playerAtRow, playerAtCol)
	def drawGrid():
		print("0	1	2	3	4\n")
		rowNum = -1
		for r in self.grid:
			rowNum += 1
			print(rowNum, "|", r)

	def getPlayerPos():
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

	def isPlayerInWorld():
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

	def drawPlayer(atRow, atCol):
		r = -1
		c = -1
		for row in self.grid:
			r += 1
			for col in row:
				c += 1
				if c == 5:
					c -= 5
				if r == atRow and c == atCol:
					self.grid[r][c] = "p"
	def movePlayer(byRow, byCol):
		row = getPlayerPos()[0]
		col = getPlayerPos()[1]
		self.grid[row][col] = "."
		self.grid[row+byRow][col+byCol] = "p"
	def movePlayerUp():
		movePlayer(-1,0)
	def movePlayerDown():
		movePlayer(1,0)
	def movePlayerRight():
		movePlayer(0,1)
	def movePlayerLeft():
		movePlayer(0,-1)	