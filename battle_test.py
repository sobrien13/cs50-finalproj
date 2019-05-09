#!/usr/bin/python3

# import appropriate libraries
import random
import sqlite3

# pre-battle setup
# import DB and player stat table
connection = sqlite3.connect("final.db") # insert correct DB name
cVar = connection.cursor()
player_health = cVar.execute("select health from player_tbl") # insert correct table name



# create enemy health and damage
def enemyStats():
	enemy_health = player_health * (random.randint(1, 6) * 1.15)
	enemy_dmg = random.randint(1, 5) * player_health
	cVar.execute("create table enemy (health, damage);")
	enemybuild = cVar.execute("insert into enemy values (?, ?)", (enemy_health, enemy_dmg))
	
	connection.commit()

enemyStats()

#list of possible enemies
List = ["Golem", "Troll", "Orc", "Ghost", "Mummy", "Goblin"]


def battle():	# I feel like battle should be its own class so we can reference the all tables from a single file
	print("You have now entered a battle!")
	e = random.randint(1, 6)
	print("From the shadows emerges a", List[e])
	sql_skills = cVar.execute("select attack from skills") # skill table needed
	result = cVar.fetchall()
	attackList = []
        for i in result:
            print(i)
        	attackList.append[i]
    attack = input("What will you do?: ")

	connection.commit()