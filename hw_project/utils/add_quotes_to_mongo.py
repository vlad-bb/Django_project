import json
from bson.objectid import ObjectId

from pymongo import MongoClient

client = MongoClient("mongodb://localhost")


db = client.hw


# with open("quotes.json", 'r', encoding="utf-8") as fd:
#     quotes = json.load(fd)

# for quote in quotes:
#     author = db.authors.find_one({'fullname': quote['author']})
#     if author:
#         db.quotes.insert_one({
#             'quote': quote['quote'],
#             'tags': quote['tags'],
#             'author': ObjectId(author['_id'])
#         })
    
# print('ok')
with open('quotes.json', 'r') as quotes_file:
    quotes = json.load(quotes_file)


def prepare_quote(quote):
    prepared_quote= ''
    prepared_quote += f"Author: {quote['author']}\n"
    prepared_quote += "Tags:\n"
    for tag in quote['tags']:
        prepared_quote += f"  #{tag}\n"
    prepared_quote += f"Quote text:\n  {quote['quote']}\n\n"
    return prepared_quote
print('ok')