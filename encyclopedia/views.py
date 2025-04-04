from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util, forms

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newpage(request):
    if request.method =="POST":
        form = forms.NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            content = content.replace("\r","") #removing carriage return for windows environment

        if title.lower() in [s.lower() for s in util.list_entries()]:
            return render(request,"encyclopedia/pageexist.html")
        else:
            util.save_entry(title, content)

    return render(request,"encyclopedia/newpage.html",{
        "form":forms.NewPageForm()
    })

def editpage(request, edit_entry):
    if request.method == "POST":
        form = forms.EditPageForm(request.POST)
        if form.is_valid():
            title = edit_entry
            content = form.cleaned_data["content"]
            content = content.replace("\r","") #removing carriage return for windows environment

        if title.lower() in [s.lower() for s in util.list_entries()]:
            util.save_entry(title, content) 
            return redirect('entrypage',edit_entry)
        else:
            return render(request,"encyclopedia/error.html")
            
    return render(request,"encyclopedia/editpage.html",{
        "form":forms.EditPageForm({'content':util.get_entry(edit_entry)}), "edit_entry":edit_entry
    })

def entrypage(request, entry):
    entry_contents = util.get_entry(entry)
    if entry_contents is None:
        return render(request,"encyclopedia/error.html")

    return render(request, "encyclopedia/entrypage.html",{
        "entry":util.markdown(entry_contents), "edit_entry":entry
    })

def search(request):
    q = request.GET.get('q')
    entries = util.list_entries()
    match = []

    for entry in entries:
        if q.lower() == entry.lower():
            return redirect('entrypage',entry)
        elif q.lower() in entry.lower():
            match.append(entry)

    return render(request, "encyclopedia/search.html",{
        "result":match
    })

def random(request):
    return redirect('entrypage',util.random_entry())