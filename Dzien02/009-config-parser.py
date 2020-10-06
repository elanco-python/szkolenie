
from configparser import ConfigParser
import json
import yaml
from pprint import pprint

# INI
config = ConfigParser()
config.read("../extras/config.ini")

sections = config.sections()
print(sections)
for section in sections:
    opts = config.options(section)
    for opt in opts:
        value = config.get(section, opt)
        print(f"sekcja={section}, opcja={opt}, wart={value}")

print("="*60)
print( config.get("General","cOmpiLeR1", fallback="BRAK") )
print("="*60)

# JSON
with open("../extras/config.json","rt") as fd:
    json_config = json.load(fd)
    print(type(json_config))
    pprint(json_config, indent=4)
    json_config["databits"] = 7
    with open("config-new.json","wt") as fd2:
        json.dump(json_config, fd2)

# YAML
print("="*80)
with open("../extras/config.yaml") as fd:
    items = list(yaml.load_all(fd, Loader=yaml.FullLoader))
    for item in items:
        print("="*60)
        for k,v in item.items():
            print(f"{k} -> {v}")
