apikey = ''

import random
import json
import requests
import time
import os
from sys import argv
import argparse



parser = argparse.ArgumentParser(prog='MarsPhotoGen', usage='Simple Program that uses the NASA API to get photos of Mars.')

parser.add_argument('-c','--count', help="Amount of photos to generate. Default is 1.", type=int, default=1)

count = parser.parse_args().count
print(parser.parse_args())

with open("./api.key", "r") as f:
    apikey = f.read()
    
    print("Using API key: " + apikey)

print("""

 /$$      /$$                               /$$$$$$$  /$$                   /$$                          /$$$$$$                     
| $$$    /$$$                              | $$__  $$| $$                  | $$                         /$$__  $$                    
| $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$| $$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$| $$  \__/  /$$$$$$  /$$$$$$$ 
| $$ $$/$$ $$ |____  $$ /$$__  $$ /$$_____/| $$$$$$$/| $$__  $$ /$$__  $$|_  $$_/   /$$__  $$ /$$_____/| $$ /$$$$ /$$__  $$| $$__  $$
| $$  $$$| $$  /$$$$$$$| $$  \__/|  $$$$$$ | $$____/ | $$  \ $$| $$  \ $$  | $$    | $$  \ $$|  $$$$$$ | $$|_  $$| $$$$$$$$| $$  \ $$
| $$\  $ | $$ /$$__  $$| $$       \____  $$| $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$ \____  $$| $$  \ $$| $$_____/| $$  | $$
| $$ \/  | $$|  $$$$$$$| $$       /$$$$$$$/| $$      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$/ /$$$$$$$/|  $$$$$$/|  $$$$$$$| $$  | $$
|__/     |__/ \_______/|__/      |_______/ |__/      |__/  |__/ \______/    \___/   \______/ |_______/  \______/  \_______/|__/  |__/
                                                                                                                                     
                                                                                                                                     
                                                                                                                                     

""")

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def start():
    try: start2()
    except: start2()

def start2():
    try: getImg()
    except: getImg()

def getImg():
    page = random.randint(1,2)
    sol = random.randint(0,50)
    data = {"page": page, "sol":sol, "api_key":apikey}
    print(data)
    time.sleep(3)
    response = requests.get(url,params=data)
    print(response)
    r = json.loads(response.text)
    r = r['photos']
    print(len(r))
    # print(r)
    r = r[random.randint(1,2)]
    img_src = r['img_src']
    img_data = requests.get(img_src)
    with open(os.path.join(os.getcwd(),'img' ,str(r['id']) + ".png", ), "xb") as f:
        f.write(img_data.content)
    

    print("Saved as " + str(r['id']) + ".png")


completed = 0

if count == 1:
    try: start()
    except: start()
elif count == 0:
    while True:
        getImg()
else:
    for _ in range(1, count):
        getImg()
