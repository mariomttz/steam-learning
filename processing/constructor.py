#!/usr/bin/python3
# -*- coding: utf-8 -*-

import mariadb
import pandas as pd


connection = mariadb.connect(
    user="root",
    password="JuipoJaguei31",
    host="127.0.0.1",
    port=3306,
    database="steam_learning"
    ) # Connection to mariadb
cur = connection.cursor()

cur.execute("select * from data") # Collect ALL data

dictforDF = {'review_range': [], 'fecha': [], 'appid': [], 'precio': [], 'Action': [],
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
            'Bullet_Hell': [], 'Top_Down': [], 'Walking_Simulator': [], 'Dungeon_Crawler': [], 'JRPG': [], 'Fighting': [], 'Colorful': []} # Dictionary for the DF creation

for data in cur:
    print(data)
    print(type(data))
    for llave in range(len(dictforDF.keys())):
        if llave < 4:
            dictforDF[list(dictforDF.keys())[llave]].append(data[llave])
        else:
            dictforDF[list(dictforDF.keys())[llave]].append(int.from_bytes(data[llave])) # Appending data to DF

DF = pd.DataFrame(dictforDF) # Creating DF

DF.to_csv("./dataset/steam_data.csv") # DF to csv