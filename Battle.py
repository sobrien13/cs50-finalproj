#!/usr/bin/python

# import appropriate libraries
import random
import sqlite3
# pre-battle setup
# import DB and player stat table
class Battle:
	playerHp = 100 #placeholder value
	enemyBaseHealth = playerHp * (random.randint(1, 6) * 1.15)
	enemies = [
		{'name' : "Golem", 'hp' : enemyBaseHealth * 1.04, 'dmg' : random.uniform(0.15, 0.22)}, #enemies[0].name -> Golem
		{'name' : "Troll", 'hp' : enemyBaseHealth * 1.08, 'dmg' : random.uniform(0.16, 0.23)},
		{'name' : "Orc", 'hp' : enemyBaseHealth * 1.1, 'dmg' : random.uniform(0.18, 0.23)},
		{'name' : "Ghost", 'hp' : enemyBaseHealth * 0.4, 'dmg' : random.uniform(0.3, 0.32)},
		{'name' : "?YouCan'tWin?", 'hp' : enemyBaseHealth * 2, 'dmg' : random.uniform(0.3, 0.4)},
	]
	def __init__(self):
		e = random.randint(1, 6)
		self.hp = enemies[e].hp
		self.name = enemies[e].name
		self.dmg = playerHp * enemies[e].dmg
		startBattle()
	def startBattle():
		print("From the shadows emerges a", name)
		#evantual function for move choice
		while self.hp > 0 and playerHp > 0:
			moves = ["Punch", "Block"] # skill table needed
			for i in moves:
				print(moves[i], "\n")
			attack = input("What will you do?: ").lower()
			if attack == "punch":
				hp -= 25 #placeholder value
				print(name, "punched for", 25, "damage.\n")
			elif attack == "block":
				print("You are blocking the next attack.\n")
			playerHp -= dmg
			print("Enemy attacks you for", dmg, "damage!\nYour hp:", playerHp, "\n")
