# Model forms
from django import forms
import datetime
from todo import models as todo_models

WIDGET_STYLE = {
    'type': 'text'
}

# Title widget
title_field = {
    "placeholder": "Input task title",
    "type": "text",
    'name': "title",
    "maxlength": 50,
    "size": 30
}

location_field = {
    "placeholder": "Input location here",
    "type": "text",
    'name': "location",
    "maxlength": 50,
    "size": 30
}

# Description widget
description_field = dict(WIDGET_STYLE)
description_field = {
    "name": "note",
    "maxlength": 1000,
    "cols": 25,
    "rows": 6
}
# Priority widget
select_field = {}

# Completed widget
completed_field = {
    "type": "checkbox",
    'class': 'form-control',
}

date_field = {
    'class': 'datepicker',
    'name': 'start_date',
    'maxlength': 80,
    'size': 30,
    'type': 'text',
    'size': '16',
}

due_date_field = {
    'class': 'datepicker',
    'name': 'due_date',
    'maxlength': 80,
    'size': 30,
    'type': 'text',
    'size': '16',
}

created_date_field = {
    'name': 'created_at',
    'maxlength': 80,
    'size': 30,
    'type': 'text',
    'size': '16',
}


event_description_field = {
    "name": "note",
    "maxlength": 1000,
    "cols": 75,
    "rows": 18,
    "style": "width: 400px; height: 85px"
}


class TaskListForm(forms.Form):
    """ Form for new list
    """
    title = forms.CharField(widget=forms.TextInput(
                            attrs=title_field))

    def __init__(self, *args, **kwargs):
        super(TaskListForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(TaskListForm, self).clean()
        return cleaned_data


class EventForm(forms.Form):
    """ Form for event
    """
    title = forms.CharField(widget=forms.TextInput(
                            attrs=title_field), required=False)

    created_date = forms.DateTimeField(input_formats=['%Y/%m/%d'], widget=forms.TextInput(
                                       attrs=created_date_field), required=False)

    description = forms.CharField(widget=forms.Textarea(
        attrs=event_description_field), required=False)

    location = forms.CharField(widget=forms.TextInput(
                               attrs=location_field), required=False)

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        #import ipdb;ipdb.set_trace()
        return cleaned_data

from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(forms.Form):
    """ Form for task model
    """
    title = forms.CharField(widget=forms.TextInput(
                            attrs=title_field))
    description = forms.CharField(widget=forms.Textarea(
        attrs=description_field), required=False)
    priority = forms.ChoiceField(widget=forms.Select(
                                 attrs=select_field))
    completed = forms.BooleanField(widget=forms.CheckboxInput(
        attrs=completed_field), required=False)

    todo_list = forms.ChoiceField(widget=forms.Select(
                                  attrs=select_field))

    start_date = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs=date_field))

    due_date = forms.DateTimeField(input_formats=['%d/%m/%Y'], widget=forms.TextInput(
        attrs=dict(due_date_field)))

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        # Populate todo list & priority
        task_list_choices = [(x.pk, x.title) for x in
                             todo_models.TaskList.objects.all()]
        self.fields['todo_list'].choices = task_list_choices
        # Retrieve priority choice from model
        self.fields['priority'].choices = todo_models.PRIORITY_CHOICES

    def clean(self):
        cleaned_data = super(TaskForm, self).clean()
        # Update completed field
        completed = cleaned_data.get("completed")
        if not completed:
            cleaned_data["completed"] = False

        return cleaned_data