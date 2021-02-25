from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from markdown2 import markdown
from . import util
from . import forms
from django.views.generic import ListView
from django.urls import reverse

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, entry_title):
    entry_title = entry_title.lower()
    entry = util.get_entry(entry_title)
    if entry == None:
        return HttpResponse("The requested entry does not exist.")
    else: 
        return render(request, "encyclopedia/entry_page.html", {
            "entry": markdown(entry),
            "entry_title": entry_title,
        })

def create_new_entry(request):
    if request.method == "POST":
        form = forms.CreateNewEntryForm(request.POST)
        if form.is_valid():
            entry_title = form.cleaned_data["title"]
            entry_content = form.cleaned_data["markdown_content"]
            entries_list = [entry.lower() for entry in util.list_entries()]
            if entry_title.lower() in entries_list:
                return HttpResponse(f'An entry with title: {entry_title} already exists')
            else:
                util.save_entry(entry_title.capitalize(), entry_content)
                return HttpResponseRedirect(reverse("wiki:entry_title", args=(entry_title,)))

        else: pass

    elif request.method == "GET":
        form = forms.CreateNewEntryForm()
    return render(request, "encyclopedia/create_new_entry.html",{
        "form": form,
    })

def edit_entry_page(request, *args, **kwargs):
    entry_title = kwargs["entry_title"]
    entry = util.get_entry(entry_title)
    entry_form_data = {
        "title": entry_title,
        "markdown_content": entry
    }
    if request.method == "GET":
        form = forms.CreateNewEntryForm(initial=entry_form_data)
    if request.method == "POST":
        form = forms.CreateNewEntryForm(request.POST)
        if form.is_valid():
            entry_title = form.cleaned_data["title"]
            entry_content = form.cleaned_data["markdown_content"]
            util.save_entry(entry_title.capitalize(), entry_content)
            return HttpResponseRedirect(reverse("wiki:entry_title", args=(entry_title,)))
    return render(request, "encyclopedia/edit_entry.html", {
        "form":form
    })

def search_results_page(request):
    entries_list = [entry.lower() for entry in util.list_entries()]
    search_term = request.GET.get("search_field")
    possible_matches = []

    for entry in entries_list:
        if search_term in entry:
            possible_matches.append(entry)

    if search_term in entries_list:
        return HttpResponseRedirect(reverse("wiki:entry_title", args=(search_term,)))

    elif possible_matches:
        return render(request, "encyclopedia/search_results.html", {
            "possible_matches": possible_matches,
            "search_term": search_term
        })
    else:
        return render(request, "encyclopedia/search_results.html", {
            "no_match": f"Your search term '{search_term}' did not match any entries.",
            "search_term":search_term
        })


    

