def csv_pred_creator(price: float, tags: list):
    # Libraries
    import pandas as pd

    # Dictionary for the data frame creation
    dictDf = {'precio': [], 'Action': [], 'Adventure': [], 'Singleplayer': [], 'Casual': [],
            'Strategy': [], 'Simulation': [], 'RPG': [], 'Multiplayer': [], 'Great_Soundtrack': [],
            'Atmospheric': [], '2D': [], 'Puzzle': [], 'Early_Access': [], 'Open_World': [], 'Story_Rich': [],
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

    for idx in dictDf.keys():
        if idx in tags:
            dictDf[idx].append(1)

        elif idx != 'precio':
            dictDf[idx].append(0)

    dictDf['precio'].append(price)

    # Creating the data frame
    df = pd.DataFrame(dictDf)

    # We declare the route
    PATH = '../processing/dataset/'

    # Data frane to csv
    df.to_csv(PATH + 'predict_data.csv')

def rating_converter(qualification: int) -> str:
    if qualification == 1:
        return 'Extremadamente negativas'

    elif qualification == 2:
        return 'Negativas'

    elif qualification == 3:
        return 'Variadas'

    elif qualification == 4:
        return 'Positivas'

    elif qualification == 5:
        return 'Extremadamente positivas'
    