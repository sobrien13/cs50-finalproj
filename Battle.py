#!/usr/bin/python
import random
import sqlite3
from Character import *
# * Creates Battle() object b -> call startBattle with b.startBattle()
# To-do to this file
	# * start battle pulls list of moves from database
	# * can either store this in Character table or other table
class Battle:
	ch = Character()
	enemyBaseHealth = 115
	enemies = [
		{'name' : "Golem", 'hp' : enemyBaseHealth * 1.04, 'dmg' : random.uniform(0.15, 0.22)}, #enemies[0].name -> Golem
		{'name' : "Troll", 'hp' : enemyBaseHealth * 1.08, 'dmg' : random.uniform(0.16, 0.23)},
		{'name' : "Orc", 'hp' : enemyBaseHealth * 1.1, 'dmg' : random.uniform(0.18, 0.23)},
		{'name' : "Ghost", 'hp' : enemyBaseHealth * 0.4, 'dmg' : random.uniform(0.3, 0.32)},
		{'name' : "?YouCan'tWin?", 'hp' : enemyBaseHealth * 2, 'dmg' : random.uniform(0.3, 0.4)},
	]
	def __init__(self):
		e = random.randint(0, 4)
		self.playerHp = 100 #placeholder val
		self.hp = int(self.enemies[e]['hp'])
		self.name = self.enemies[e]['name']
		self.dmg = int(self.playerHp * self.enemies[e]['dmg'])
	def startBattle(self):
		print("From the shadows emerges a", self.name)
		#evantual function for move choice
		while 1:
			#skill table needed
			# move and damage values are placeholders
			attack = input("What will you do? (Punch, Block): ").lower()
			if attack == "punch":
				self.hp -= 25 #placeholder value
				print(self.name, "punched for", 25, "damage.\n")
				self.playerHp -= self.dmg
			elif attack == "block":
				print("You are blocking the next attack.\n")
				self.dmg *= 0.5
				self.playerHp -= self.dmg
			if attack == "block":
				print("Enemy attacks you for", self.dmg, "damage!\nYour hp:", self.playerHp, "\n")
				self.dmg *=2
			else:
				print("Enemy attacks you for", self.dmg, "damage!\nYour hp:", self.playerHp, "\n")
			print(self.name, "hp:", self.hp)
