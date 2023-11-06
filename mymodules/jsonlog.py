import json
import os

from datetime import datetime

def jsonlog(fpath:str, data:dict):
    if not os.path.isfile(fpath):
        with open(fpath, "w") as f:
            json.dump({}, f)

    with open(fpath, "r+") as f:
        jsons = json.load(f)
        jsons[f"{datetime.now()}"] = data
        f.seek(0)
        json.dump(jsons, f, ensure_ascii=False, indent=4)
