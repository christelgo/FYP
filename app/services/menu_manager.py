import json
import os  
import re

def prepare_menu(items):
    for item in items:
        item["base_id"] = re.sub(
            r'[^a-z0-9]+',
            "_",
            item["name"].lower()
        ).strip("_")

        if item.get("set_key"):
            item["type"] = "bento"
        else:
            item["type"] = "ala_carte"
        
    return items

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MENU_PATH= os.path.join(BASE_DIR,"data", "menu_items.json")

with open(MENU_PATH,"r", encoding="utf-8" ) as f:
    MENU = json.load(f)
