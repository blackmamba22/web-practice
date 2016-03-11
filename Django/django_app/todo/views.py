from django.shortcuts import render, redirect

from . import forms, models
# Create your views here.

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
