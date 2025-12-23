import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MENU_PATH= os.path.join(BASE_DIR,"data", "menu_items.json")

with open(MENU_PATH,"r", encoding="utf-8" ) as f:
    MENU = json.load(f)

print("MENU LOADED KEYS:", MENU.keys())
print("chick ala KEYS:", MENU["categories"]["ala_carte"]["chicken"])