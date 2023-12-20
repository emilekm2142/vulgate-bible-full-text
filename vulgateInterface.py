import requests, re, json
from bs4 import BeautifulSoup
def load_bible_cache():
    #load from json file
    with open("bible.json", "r") as f:
        bible = json.load(f)
    return bible
def save_bible_cache(bible):
    #save to json file
    with open("bible.json", "w") as f:
        json.dump(bible, f)
bible = {
    "Genesis":[[],[]]
}

bible = load_bible_cache()
print(bible["Genesis"][0][0]) #print first verse of Genesis
print(bible["Genesis"][0][1]) #print second verse of Genesis
print(bible["Genesis"][1][0]) #print first verse of Genesis chapter 2

#get all book titles
book_titles = list(bible.keys())
print(book_titles)


def get_plain_text():
    plain_text = ""
    for book_title in book_titles:
        for chapter in bible[book_title]:
            plain_text+= " ".join(chapter)
    return plain_text

plain_text = get_plain_text()
#save plain text to file
with open("bible.txt", "w") as f:
    f.write(plain_text)