#!/usr/bin/python
#Establishes communication with Game.py
#Player position should probably be stored in 'save.db' and loaded through Game.py
#Evantual integration with enemy code to determine when/where battles begin
#Could store positions of enemy as integers row and col in 'save.db'
class World:
	grid = 	[["~", "~", "~", "~", "~"], 
			["~", "~", "p", "~", "~"], 
			["~", "~", "~", "~", "~"], 
			["~", "~", "~", "~", "~"], ]
	def getPlayerPos():
		#Returns tuple which contains player position
		#Should return 1,2
		r = -1
		c = -1
		for row in world:
			r += 1
			for col in row:
				c += 1
				if c == 5:
					c -= 5
				if col == "p":
					return r, c
	def movePlayerUp():
		#Changes location of 'p' in world arr
		#New character representing traveled space "."
		#INCOMPLETE
		row = getPlayerPos()[0] 
		col = getPlayerPos()[1] 
		world[row][col] = "."
		world[row-1][col] = "p"
		print(world[row-1][col])

		