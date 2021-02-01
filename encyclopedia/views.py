from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry_title):
    entry = util.get_entry(entry_title)
    if entry == None:
        return HttpResponse("The requested entry does not exist.")
    else: 
        return render(request, "encyclopedia/entry_page.html", {
            "entry": util.get_entry(entry_title),
            "entry_title": entry_title
        })
