
import requests
import time
from colorama import Fore, Style
        
QUIT=False

while QUIT==False:
    userinput = input("Enter the name of pokemon : ").lower()
    print("")
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{userinput}")
    if req.status_code==200:
        pokemon = req.json()
        print("Name : " ,Fore.CYAN + Style.BRIGHT+ pokemon["name"])
        print(Style.RESET_ALL)
        print('Abilities:')
        for abilities in pokemon["abilities"]:
            print("\t",Fore.WHITE +Style.BRIGHT+ abilities['ability']['name'])
            time.sleep(0.5)
        print(Style.RESET_ALL,"\n")
        ask = input("Want to quit (yes or no): ")
        if ask=="yes":
            QUIT=True
        elif ask=="no":
            QUIT=False
        else:
            print("Just Continue !! XD\n")

    else:
        print(Fore.RED+Style.BRIGHT+'\npokemon not found')
        print(Style.RESET_ALL)
        ask = input("Want to quit (yes or no): ")
        if ask=="yes":
            QUIT=True
        elif ask=="no":
            QUIT=False
        else:
            print("Just Continue !! XD\n")
        

