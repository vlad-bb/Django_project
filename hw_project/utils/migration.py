import os 
import django

from pymongo import MongoClient

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author # noqa


client = MongoClient('mongodb://localhost:27017')

db = client.hw

authors = db.authors.find()

for author in authors:
    #print(author)
    Author.objects.get_or_create(
        fullname=author['fullname'],
        date_born=author['date_born'],
        location_born=author['location_born'],
        bio=author['bio']
    )
# quotes = db.quotes.find()

# for quote in quotes:
#     print(quote['tags'])