# script to convert the json data sent from the site to a more readable form

# could be simplified a lot but just wanted to make something quickly

import json

files = ["accessories", "bottoms", "hatshelmets", "misc", "shoes", "tops"]

for file in files:
    with open(f"mtf/{file}.json", "r") as f:
        buffer = []
        data = json.load(f)
        for item in data:
            buffer.append({
                "Male Category": item['value']['malecategory'],
                "Male Clothing": item['value']['maleclothing'],
                "Female Category": item['value']['femalecategory'],
                "Female Clothing": item['value']['femaleclothing']
            })

            with open(f"mtf/out2/{file}.json", "w+", encoding="utf-8") as outfile:
                outfile.write(str(buffer))

    with open(f"ftm/{file}.json", "r") as f:
        buffer = []
        data = json.load(f)
        for item in data:
            buffer.append({
                "Female Category": item['value']['femalecategory'],
                "Female Clothing": item['value']['femaleclothing'],
                "Male Category": item['value']['malecategory'],
                "Male Clothing": item['value']['maleclothing']
            })

            with open(f"ftm/out2/{file}.json", "w+", encoding="utf-8") as outfile:
                outfile.write(str(buffer))
