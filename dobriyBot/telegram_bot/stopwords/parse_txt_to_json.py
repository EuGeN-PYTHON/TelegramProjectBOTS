import json

stop_words = []

with open('stopwords.txt', encoding='utf-8') as data:
    for words in data:
        stop_words = words.split(' ')

with open('cenz.json', 'w', encoding='utf-8') as data:
    json.dump(stop_words, data)
