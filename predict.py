import os
import json
import sys
import time


temp = {"total_guesses": 0, "total_correct": 0, "userchoices": [], "userchoices_chunks": [], "number_counter": {}}
        
current_window = 0
ascii_art =     """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░ 
░░░░░░████████▓████▓███▓██████▓██▓██▓▓▓▓██▓░░░░░░░ 
░░░░░░▒▒▒██▒▒▒▓█▒▒▒▓█▒▒████▓▒▒▓▓▒▓▒▓▓▓▓█▒▒░░░░░░░░ 
░░░░░░░░░██░░░▓█░░▒█▓░▓████▓░░█▓▒█▒▓██▓█▓▒░░░░░░░░ 
░░░░░░░░▓██▓░░▓█▓░██░██▒░░▒██░█▓▒█▒▓█░░▒██░░░░░░░░ 
░░░░░░░░████░░░██░██░▓▓░██░▓▓░█▓▒█▒▓█▒░░██░░░░░░░░ 
░░░░░░░▒█▒▒█▓░░██▓█▒░▓▓░██░▓▓░█▓▒█▒▓█▒░░██░░░░░░░░ 
░░░░░░░█▓░░▓▓░░▒██▓░░▓█▓░░▓█▓░█▓▒█▒▓█░░▒██░░░░░░░░ 
░░░░░░▒█▓▓▓▓█▒░░██▓░░░▓█▓▓█▓░░█▓▒█▒▓█▓▓█▓░░░░░░░░░ 
░░░░░░▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▓████▒▒▒▓▓▓▓▓▓▓▓▓█▒▒▒░░░░░░░ 
░░░░░░██▓▓▓▓▓████▓██████▓▓▓███▓██▓██▓▓▓▓██▓░░░░░░░ 
░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 
"""

os.system("cls")

def initNumberModule():
    
    with open("{}/dataset.json".format(sys.path[0]), "r", encoding="utf-8") as file:
        data = json.load(file)
        for key in data.keys():
            temp[str(key)] = data[str(key)]
        
    os.system("cls")
    print("You can start entering numbers between 1-9.")
    while True:
        new_choice = input()
        possible = []
        os.system("cls")
        if new_choice.isnumeric():
            if 1 <= int(new_choice) <= 9:
                temp["total_guesses"] += 1
                temp["number_counter"][str(new_choice)] = temp["number_counter"].get(str(new_choice), 0) + 1
                temp["userchoices"].append(new_choice)
                if len(temp["userchoices"]) >= 3:
                    chunk = temp["userchoices"][-3:]
                    temp["userchoices_chunks"].append(chunk)
                    for previous_chunk in temp["userchoices_chunks"][:-1]:
                        if previous_chunk[:2] == chunk[:2]:
                            possible.append(previous_chunk[2]) 
        if possible:
            prediction = sorted(possible, key=lambda x: possible.count(x), reverse=True)[0]
            if int(prediction) == int(new_choice):
                temp["total_correct"] += 1
                print("\nI got it right!\nYou entered {}, my prediction was {}!\nSuccess Rate: {}%".format(new_choice, prediction, (round((temp["total_correct"] / temp["total_guesses"]) * 100)) or 0))
            else:
                print("\nI got it wrong!\nYou entered {}, my prediction was {}!\nSuccess Rate: {}%".format(new_choice, prediction, (round((temp["total_correct"] / temp["total_guesses"]) * 100)) or 0))
        else:
            print("\nI couldn't predict this!\nYou entered {}!\nSuccess Rate: {}%".format(new_choice, (round((temp["total_correct"] / temp["total_guesses"]) * 100)) or 0))
        with open("{}/dataset.json".format(sys.path[0]), "w", encoding="utf-8") as file:
            json.dump(temp, file, indent=3)

def resetDataset():
    os.system("cls")
    while True:
        proceed = input("Do you really want to reset the collected dataset? This action is irreversible! (Y/N)\n")
        if proceed.lower() == "y":
            os.system("cls")
            temp = {"total_guesses": 0, "total_correct": 0, "userchoices": [], "userchoices_chunks": [], "number_counter": {}}
            with open("{}/dataset.json".format(sys.path[0]), "w", encoding="utf-8") as file:
                json.dump(temp, file, indent=3)
            print("Dataset has been reset.\nWait 5s to return to main menu...")
            break
        elif proceed.lower() == "n":
            os.system("cls")
            print("Reset has been canceled.\nWait 5s to return to main menu...")
            break
        else:
            print("Invalid input. Try again.")
            
    time.sleep(5)
    os.system("cls")
    initGreeting()
    
def initGreeting():
    greetingmessage = "Welcome to the number predicter by AVOIID.\nHow do you want to proceed?\n"
    options = [
        "1. Start the model",
        "2. Read dataset stats (WIP)",
        "3. Reset dataset (WIP)"
    ]
    text_cache = ""
    for line in ascii_art.splitlines():
        print(line)
        time.sleep(0.05)
    for index, letter in enumerate(greetingmessage):
        os.system("cls")
        text_cache += letter
        print(ascii_art + "\n" + text_cache + ("|" if not index == len(greetingmessage)-1 else ""))
        time.sleep(0.02)
    for option in options:
        print(option)
        time.sleep(0.5)
    while True:
        try:
            selection = input("\nChoose an option: ")
            if selection.isdigit() and int(selection) in [1, 2, 3]:
                selection = int(selection)
                break
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    if selection == 1:
        initNumberModule()
    elif selection == 2:
        print("Reading dataset stats is currently a work in progress.")
    elif selection == 3:
        resetDataset()
initGreeting()