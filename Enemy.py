#!/bin/us/python3
import random
import sqlite3
import Game
import Character
# pre-battle setup
# import DB and player stat table
class Enemy:
	connection = Game.connection # insert correct DB name
	c = connection.cursor()
	player_health = c.execute("select health from player_tbl") # insert correct table name

	# create enemy health and damage
	def initStats(player_health):
		health = player_health * (random.randint(1, 6) * 1.15)
		dmg = random.randint(1, 5) * player_health
		c.execute("create table Enemy (health, damage);")
		c.execute("insert into Enemy values (?, ?)", (enemy_health, enemy_dmg))
	initStats()

