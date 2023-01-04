import random as rd


theGuy: dict = {1:7,2:21,3:22,4:30,5:18,6:12,7:16,8:21,9:18,10:23,
    11:22,12:21,13:18,14:20,15:20,16:20,17:20,18:20,19:30,20:20,21:10} # as of 12/22/2022
thePark: dict = {1:13,2:18,3:17,4:17,5:14,6:17,7:15,8:14,9:14,10:14,
    11:14,12:14,13:14,14:14,15:14,16:14,17:10,18:10,19:10,20:10,21:10,22:10,23:10} # as of 12/28/2022
theDad: dict = {1:7,2:16,3:19,4:16,5:20,6:18,7:19,8:18,9:19,10:20,
    11:3,12:15,13:22,14:22,15:22,16:22,17:22,18:22,19:22} # as of 12/28/2022
leave: dict = {1:6,2:6} # as of 1/3/2022

def Season_Episode(show: dict) -> list:
    season: int = rd.randint(1,len(show))
    episode: int = rd.randint(1,show[season])
    return([season,episode])

def Show_Picker() -> list:
    show_list: list(dict) = [theGuy,thePark,theDad]
    show_num: int = rd.randint(1,4)
    return show_list[show_num-1]