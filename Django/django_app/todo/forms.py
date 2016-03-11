from django import forms
from todo.models import ToDoItem

class ToDoForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label="Action Item")
    due_date = forms.DateTimeField(label="Due Date", required=False)

    class Meta:
        model = ToDoItem
        fields = ('name','due_date')
