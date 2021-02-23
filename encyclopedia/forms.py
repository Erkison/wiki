from django import forms

class SearchForm(forms.Form):
    search_field = forms.CharField(label=False, widget=forms.TextInput(attrs={"placeholder": "Search",
    "class":"form-control border border-dark",
    }))

class CreateNewEntryForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        "class":"form-control border border-dark"
    }))
    markdown_content = forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control border border-dark"
    }))