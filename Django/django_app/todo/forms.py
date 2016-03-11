from django import forms
from todo.models import ToDoItem

class ToDoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, help_text="Add to-do item.")
    due_date = forms.DateTimeField(widget=forms.DateTimeInput)

    class Meta:
        model = ToDoItem
        fields = ('name',)
