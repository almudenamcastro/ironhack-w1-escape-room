# **Escape Room**
## *First collaborative project from Data Analysis Bootcamp from Ironhack*
This repository is part of the Data Analysis bootcamp taught by Ironhack, specifically, this is the first project.

It presents a map with four rooms (home, bedroom 1, bedroom 2 and living room) that, although connected, have all their doors closed. The objective of the game is to get out of the house by collecting all the keys.
# Tools
This first project focuses on learning, applying and improving the logic of Python base programming. The ecosystem we have used is Google Collab to share code among peers and Visual Studio Code to test in isolation certain parts of the code.

***Goals***
The first objective was to learn how to work in both Google Collab and GitHub ecosystems to not only foster teamwork but to familiarize ourselves with the differences between them.

The second was to apply the knowledge learned during the week (1) of the bootcamp. Therefore, the focus has been on making robust code as clean as possible, applying what we have learned about “good code”. 

The third one was to create and develop a code (from a prototype given by the teachers) following the logic of the Escape Room game. At the very least, the game was expected to be able to be finished and run smoothly.

# Issues
Throughout the four days of development we have faced different problems that we have managed, a priori, to solve.

The most notable is that at first we made the code based on two global variables, something that, although it allowed us to execute it, meant that the functions were not well developed (at least in terms of cleanliness and robustness of the code). 

Specifically, we were defining *game_state* and *object_relations* outside the functions without passing them as parameters. Finally, we decided to develop and include *game_state* and *object_relations* variables in all functions that use them to avoid relying on global variables.

The second conflict we encountered was that, after finishing the game, the “What would you like to examine?” message kept popping up as input. The solution we found was twofold: **1)** we added a `return` in the game end condition within the `play_room` function **2)** enforce the condition for which the “What would you like to examine?” question pops up. :

```python
else:
    if game_state[“current_room”] != game_state[“target_room”]:
    examine_item(input("What would you like to examine? ”).strip(), game_state, object_relations)
```

# Deliverables

* `functionsb.py`, contains all the functions
* `main.ipynb`, contains the objects and the solution

## Link

You can get access to the Escape Room from Google Collab [here](https://colab.research.google.com/drive/1RuM_ABfVHSQ-QQeeaj8Dg1UypzTK42eT).

Get access to [functions.py](https://drive.google.com/file/d/11UHKeciDuAOvT2lTjYcZ0wFiVAcvvb-D/view)

Get access to [main.ipynb](https://colab.research.google.com/drive/1RuM_ABfVHSQ-QQeeaj8Dg1UypzTK42eT)

You can watch the slide's presentations [here](https://gamma.app/docs/Proyecto-Scape-Room-Buenas-Practicas-en-Python-s2n9n7o1l7p145h?follow_on_start=true&following_id=2eqqtx5ltya8esx&mode=doc)

## Participants

* [Almudena Castro](https://github.com/almudenamcastro)
* [Óscar Sánchez](https://github.com/Osanchezr)
* [Danny Rodas](https://github.com/cohet3)
* [Luis H. Rodríguez](https://github.com/LuisHRF)

## Map
![](https://github.com/almudenamcastro/ironhack-w1-escape-room/blob/main/escape_room_map_ironhack.png)

