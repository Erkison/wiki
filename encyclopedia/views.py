from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import markdown
from . import util
from . import forms
from django.views.generic import ListView

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
            "entry": markdown(entry),
            "entry_title": entry_title
        })

def search_results_page(request):
    entries_list = [entry.lower() for entry in util.list_entries()]
    search_term = request.POST.get("q", "").lower()
    possible_matches = []

    for entry in entries_list:
        if search_term in entry:
            possible_matches.append(entry)

    if search_term in entries_list:
        return HttpResponseRedirect(f"encyclopedia/{search_term}")

    elif possible_matches:
        return render(request, "encyclopedia/search_results.html", {
            "possible_matches": possible_matches,
            "search_term": search_term
        })
    else:
        return render(request, "encyclopedia/search_results.html", {
            "no_match": f"Your search terms '{search_term}' did not match any entries."
        })


    

