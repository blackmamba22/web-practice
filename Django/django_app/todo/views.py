from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect

from . import forms, models
# Create your views here.

@csrf_protect
def index(request):
    todo_list = models.ToDoItem.objects.all()

    if request.method == 'POST':
        form = forms.ToDoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # reset the form and return to index page
            form = forms.ToDoForm()
            return render(request, 'todo/index.html', {'form': form, 'todo': todo_list})
        else:
            print form.errors
    else:
        form = forms.ToDoForm()

    return render(request, 'todo/index.html', {'form': form, 'todo': todo_list})

def remove_item(request):
    if request.method == 'POST':
        del_item = request.POST.get("remove_button", "nothing found")

        if not del_item == "nothing found":
            m = models.ToDoItem.objects.get(id=del_item)
            print m
            m.delete()

    if 'next' in request.GET:
        return redirect(request.GET['next'])
    return render(request, 'todo/base.html')

@csrf_protect
def mark_complete(request):
    if request.method == 'POST':
        completed_item = request.POST.get("data", "nothing found")
        print completed_item
        #if not completed_item == "nothing found":

    return render(request, 'todo/base.html')
