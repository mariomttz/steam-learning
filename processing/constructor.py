#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import pandas as pd
import db_config
import mariadb

# DB connector settings
# References https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
# For this part of the code

#Connect to MariaDB
try:
    conn = mariadb.connect(
        user = db_config.setting['user'],
        password = db_config.setting['password'],
        host = db_config.setting['host'],
        port = db_config.setting['port'],
        database = db_config.setting['database']
    )

except mariadb.Error as e:
    sys.exit(1)

# Get the cursor
cur = conn.cursor()

# End part of code

# Collect all data from the db
cur.execute("select * from data;")

# Dictionary for the data frame creation
dictDf = {'review_range': [], 'fecha': [], 'appid': [], 'precio': [], 'Action': [],
            'Adventure': [], 'Singleplayer': [], 'Casual': [], 'Strategy': [], 'Simulation': [],
            'RPG': [], 'Multiplayer': [], 'Great_Soundtrack': [], 'Atmospheric': [],
            '2D': [], 'Puzzle': [], 'Early_Access': [], 'Open_World': [], 'Story_Rich': [],
            'Co_op': [], 'Difficult': [], 'Shooter': [], 'Sci_fi': [], 'First_Person': [],
            'Horror': [], 'VR': [], 'Anime': [], 'Pixel_Graphics': [], 'Funny': [], 'Fantasy': [],
            'Platformer': [], 'Female_Protagonist': [], 'Free_to_Play': [], 'FPS': [], 'Survival': [],
            'Gore': [], 'Violent': [], 'Sandbox': [], 'Retro': [], 'Arcade': [], 'Comedy': [], 'Classic': [],
            'Nudity': [], 'Third_Person': [], 'Massively_Multiplayer': [], 'Exploration': [],
            'Point_and_Click': [], 'Visual_Novel': [], 'Turn_Based': [], 'Space': [], 'Sports': [],
            'Rogue_like': [], 'Tactical': [], 'Cute': [], 'Racing': [], 'Psychological_Horror': [],
            'Online_Co_Op': [], 'Zombies': [], 'Family_Friendly': [], 'Sexual_Content': [], 'Local_Co_Op': [],
            'Local_Multiplayer': [], 'Controller': [], 'Replay_Value': [], 'Memes': [], 'Building': [], 'RTS': [],
            'Turn_Based_Strategy': [], 'Side_Scroller': [], 'Fast_Paced': [], 'Crafting': [], 'Action_RPG': [],
            'Mystery': [], 'Shoot_Em_Up': [], 'Dark': [], 'Management': [], 'Survival_Horror': [], 'Hack_and_Slash': [],
            'War': [], 'Historical': [], 'Physics': [], 'Stealth': [], 'Rogue_lite': [], 'PvP': [], 'Realistic': [],
            'Short': [], 'Isometric': [], 'RPGMaker': [], 'Moddable': [], 'Relaxing': [], 'Third_Person_Shooter': [],
            'Bullet_Hell': [], 'Top_Down': [], 'Walking_Simulator': [], 'Dungeon_Crawler': [], 'JRPG': [], 'Fighting': [], 'Colorful': []} 

for data in cur:
    for llave in range(len(dictDf.keys())):

        if llave < 4:
            dictDf[list(dictDf.keys())[llave]].append(data[llave])

        else:
            # Appending data to the data frame
            dictDf[list(dictDf.keys())[llave]].append(int.from_bytes(data[llave]))

# Creating the data frame
df = pd.DataFrame(dictDf)

# We declare the route
PATH = './processing/dataset/'

# Data frane to csv
df.to_csv(PATH + "steam_data.csv")

# Close Connection
conn.close()