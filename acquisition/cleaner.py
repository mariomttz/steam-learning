#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cleaner_data(json_string:str,date:str):
    import json
    from review import rangeCalculator # Import the calcualtor for the tag
    # The game tags we will use
    realTags = ['Action', 'Adventure', 'Singleplayer', 'Casual', 'Strategy',
                'Simulation', 'RPG', 'Multiplayer', 'Great Soundtrack', 'Atmospheric',
                '2D', 'Puzzle', 'Early Access', 'Open World', 'Story Rich',
                'Co-op', 'Difficult', 'Shooter', 'Sci-fi', 'First-Person',
                'Horror', 'VR', 'Anime', 'Pixel Graphics', 'Funny',
                'Fantasy', 'Platformer', 'Female Protagonist', 'Free to Play', 'FPS',
                'Survival', 'Gore', 'Violent', 'Sandbox', 'Retro',
                'Arcade', 'Comedy', 'Classic', 'Third Person', 'Nudity',
                'Massively Multiplayer', 'Exploration', 'Point & Click', 'Visual Novel', 'Turn-Based',
                'Space', 'Sports', 'Rogue-like', 'Tactical', 'Cute',
                'Racing', 'Psychological Horror', 'Online Co-Op', 'Zombies',
                'Family Friendly', 'Sexual Content', 'Local Co-Op', 'Local Multiplayer', 'Controller',
                'Replay Value', 'Memes', 'Building', 'RTS', 'Turn-Based Strategy',
                'Side Scroller', 'Fast-Paced', 'Crafting', 'Action RPG', 'Mystery',
                'Dark', "Shoot 'Em Up", 'Management', 'Survival Horror', 'Hack and Slash',
                'War', 'Historical', 'Physics', 'Stealth', 'Rogue-lite',
                'PvP', 'Realistic', 'Short', 'Isometric', 'Moddable',
                'RPGMaker', 'Third-Person Shooter', 'Relaxing', 'Bullet Hell', 'Top-Down',
                'Walking Simulator', 'Dungeon Crawler', 'JRPG', 'Fighting', 'Colorful']
    diction = json.loads(json_string) # Convert the string to a dictionary
    sql1 = "INSERT INTO data (review_range, fecha, appid, precio, " # Create the first half of the sql instruction
    sql2 = ") VALUES (" + str(rangeCalculator([diction["positive"],diction["negative"]])) + ", " + date + ", " + str(diction["appid"])+ ", " + diction["price"] + ", " # Create the second half of the sql
    for idx in diction["tags"].keys():
        if idx in realTags:
            if " " in idx:
                idx = idx.replace(" ","_") # Replace unwanted characters on the tags
            if "-" in idx:
                idx = idx.replace("-","_")
            if "'" in idx:
                idx = idx.replace("'","")
            if "&" in idx:
                idx = idx.replace("&","and")
            sql1 = sql1 + idx + ", " # Add tags and values
            sql2 = sql2 + "1, "
    sql1 = sql1[:-2] # Remove the last ", "
    sql2 = sql2[:-2]
    sqlR = sql1 + sql2 + ");" # Unify the instruction and return it.
    return sqlR
