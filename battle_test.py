#!/bin/us/python3
import random
import sqlite3

# pre-battle setup
# import DB and player stat table
connection = sqlite3.connect("final.db") # insert correct DB name
c = connection.cursor()
player_health = c.execute("select health from player_tbl") # insert correct table name

# create enemy health and damage
def enemyStats(player_health):
	enemy_health = player_health * (random.randint(1, 6) * 1.15)
	enemy_dmg = random.randint(1, 5) * player_health
	c.execute("create table Enemy (health, damage);")
	enemybuild = c.execute("insert into Enemy values (?, ?)", (enemy_health, enemy_dmg))
	connection.commit()
enemyStats()

