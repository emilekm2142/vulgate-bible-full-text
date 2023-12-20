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

base_url = "https://sacred-texts.com/bib/vul/"
index_url = "https://sacred-texts.com/bib/vul/index.htm"
req = BeautifulSoup(requests.get(index_url).text)
books = req.find_all("a")
genesis_index = books.index(req.find("a", string="Genesis"))
print(genesis_index)
books = books[genesis_index:]
print(books)
for book in books:
    book_url = base_url + book["href"]
    book_index = BeautifulSoup(requests.get(book_url).text)
    print(book_url)
    #filter out all links that dont contain the word "chapter"
    chapters = book_index.find_all("a", string=lambda text:text is not None and  "chapter" in text.lower())
    book_title = book.text
    bible[book_title] = []
    print(chapters)
    for chapter in chapters:
        chapter_url = base_url + chapter["href"]
        chapter_index = BeautifulSoup(requests.get(chapter_url).text)
        chapter_title = chapter.text
        print(chapter_url)
        verses = chapter_index.find_all("p")
        pure_verses = []
        for verse in verses:
            #remove first digits from verse with regex
            regex = re.compile(r"^\d+")
            verse = regex.sub("", verse.text)
            #remove non-breaking spaces
            verse = verse.replace('\xa0', ' ')
            verse = verse.replace('\n', '')
            pure_verses.append(verse)
        bible[book_title].append(pure_verses)
    save_bible_cache(bible)