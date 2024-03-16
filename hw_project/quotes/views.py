from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .utils import get_mongodb



def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context= {'quotes': quotes_on_page})


quotes = db.quotes.find()


for quote in quotes:
    print(quote.tags)