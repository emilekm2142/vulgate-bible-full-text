import requests, re, json
from bs4 import BeautifulSoup
def load_bible_cache():
    #load from json file
    with open("bible.json", "r") as f:
        bible = json.load(f)
    return bible
def save_bible_cache(bible, version=""):
    #save to json file
    with open(f"bible{version}.json", "w") as f:
        json.dump(bible, f)
bible = {
    "Genesis":[[],[]]
}

def fix_verse(verse):
    return verse.lstrip().replace("\u00e6", "ae").replace("\u00eb", "e").replace("\u009c", "oe")

bible = load_bible_cache()
new_bible = {}
for book_title in bible:
    new_bible[book_title] = []
    for chapter in bible[book_title]:
        new_bible[book_title].append([])
        for verse in chapter:
            verse = fix_verse(verse)
            new_bible[book_title][-1].append(verse)
save_bible_cache(new_bible, "fixed")
