from django.shortcuts import render, redirect

from . import forms, models
# Create your views here.

def index(request):

    if request.method == 'POST':
        form = forms.ToDoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('index')
        else:
            print form.errors
    else:
        form = forms.ToDoForm()

    todo_list = models.ToDoItem.objects.all()
    return render(request, 'todo/index.html', {'form': form, 'todo': todo_list})
