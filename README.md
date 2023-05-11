<h1 align="center">Steam learning</h1>

![banner](./docs/img/banner.png)

## Members 🕹️
- Ashley Dafne Aguilar Salinas - UNAM ENES Morelia 
- Jorge Jacuinde Mayés - UNAM ENES Morelia
- Mario Alberto Martinez Oliveros - UNAM ENES Morelia

## Introduction 📜
The video game industry is one of the largest branches of the market today, in Mexico alone revenues increased from 0.84 billion dollars to 1.73 in 2012 [(Staff, 2022)](https://www.forbes.com.mx/la-industria-del-videojuego-en-mexico-represento-1-73-billones-de-dolares-en-2021/), for this and many other reasons, the industry is a great sea of possibilities for software developers.  

Steam is the number one platform in the online video game purchase and distribution market, with more than 30 thousand games in its catalog, it is one of the best options for gamers worldwide to find video games and for developers to publish and distribute their projects on the platform [(Steam, The Ultimate Online Game Platform)](https://store.steampowered.com/about/).  

SteamSpy is a website that, although not directly linked to Valve, the company behind Steam, does have an API of the platform and more importantly, has a sub-API that provides only the information of the games, but not of the players or other private characteristics of Steam users [(Games sales)](https://steamspy.com/about).  

## Justification ⚖️
Steam learning is a tool that, through characteristic data of games on Steam, predicts a possible public opinion score to support developers in the process of creation or distribution to get an idea of those trends or ideas that work best in different types of games with just the input of the characteristics of their own.

## Overall objective 🤖
The creation of an AI model that predicts the rating by the audience of some potential video game on Steam.

## Particular objectives 🎮
- The model will be validated and trained only with data from "Indie" games, i.e., Independent from some big developer.
- Characteristic tags of the games will be used as attributes, as long as the tag is used more than 145 times in all Steam.
- The creation of a promt, so that users can enter the data of their games for the model to predict their possible review on Steam.

## Software tools to use 💾
- Primary programming language: **Python 3**
- Secondary programming language: **Bash**
- Primary Python libraries to use:
    - NumPy
    - Pandas
    - Sklearn
    - JSON
The API we will use will be the one provided by ["SteamSpy"](https://steamspy.com/).

## Architecture 🧭
### Acquisition 📥
It will be the module in charge of obtaining data from the API, through the programming of a data acquirer, which will be executed every day.

### Storage 🫙
This module will store the "raw" data to be obtained from the API, to be later cleaned by another program, and stored again for later use.

### Processing ⚙️
It will be the module that will provide the necessary algorithms for the creation of the CSVs for the training of the AI model that we will use for the prediction. As well as it will also be in charge of creating the algorithm that will train and execute the AI model.

### Publication 💻
In this module we will host both the "promt" where you can access the model predictions as a user and the about page of the same project.

## References 🔍
- Staff, F. (2022). Mexico's video game industry accounted for $1.73 billion in 2021. Forbes Mexico [https://www.forbes.com.mx/la-industria-del-videojuego-en-mexico-represento-1-73-billones-de-dolares-en-2021/](https://www.forbes.com.mx/la-industria-del-videojuego-en-mexico-represento-1-73-billones-de-dolares-en-2021/).
- Steam, The Ultimate Online Game Platform. [https://store.steampowered.com/about/](https://store.steampowered.com/about/). 
- Games sales. SteamSpy - All the data about Steam games [https://steamspy.com/](https://steamspy.com/).
