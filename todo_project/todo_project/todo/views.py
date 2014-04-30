# Function based view
import json
from django.http import HttpResponse

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext
import datetime
from todo import utils
from todo.models import TaskList
from todo.models import Event
from todo.models import Task
from todo.forms import TaskListForm
from todo.forms import TaskForm
from todo.forms import EventForm


def task_delete(request, id):
    """ Delete a task
    """
    template_name = 'task_delete_confirm.html'
    task = get_object_or_404(Task, pk=id)

    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect(reverse('todo.views.task_list'))

    return render_to_response(template_name, {'task': task},
                              context_instance=RequestContext(request))


def task_update(request, id):
    """ Update a task
    """
    template_name = 'task_update.html'
    task = get_object_or_404(Task, pk=id)

    print "method %r" % request.method
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        print "form valid %r" % form.is_valid()
        if form.is_valid():
            start_date = form.data.get('start_date')
            if start_date:
                start_date = datetime.datetime.strptime(start_date, '%d/%M/%Y')
            else:
                start_date = None
            due_date = form.data.get('due_date')
            if due_date:
                due_date = datetime.datetime.strptime(due_date, '%d/%m/%Y')
            else:
                due_date = None

            completed = form.data.get('completed')
            if not completed:
                completed = False

            task.title = form.data.get('title')
            task.start_date = start_date
            task.due_date = due_date
            task.completed = completed
            task.todo_list_id = form.data.get('todo_list')
            task.priority = form.data.get('priority')

            task.save()
            return HttpResponseRedirect(reverse('todo.views.task_list'))

    return HttpResponseRedirect(reverse('todo.views.task_list'))


def task_list(request):
    """ List status of all todo items
    """
    task_listing = []
    for todo_task in TaskList.objects.all():
        todo_dict = {}
        todo_dict['list_object'] = todo_task

        tasks = []
        for task in todo_task.task_set.all():
            task_map = task.__dict__
            task_map['start_date'] = task_map['start_date'].strftime('%d/%M/%Y')
            task_map['form'] = TaskForm(initial=task_map)
            tasks.append(task_map)
        todo_dict['list_tasks'] = tasks
        todo_dict['item_count'] = todo_task.num_tasks()
        todo_dict['items_complete'] = todo_task.num_tasks_completed()
        todo_dict['percent_complete'] = todo_task.percent_completed()
        task_listing.append(todo_dict)


    print "Task listing %r" % task_listing

    return render_to_response('tasks.html', {'task_listing': task_listing},
                              context_instance=RequestContext(request))


def create_event(request):
    """ Create new event.
    """
    import ipdb;ipdb.set_trace()

    print "Create new event"
    if request.method == 'POST':
        post_obj = request.POST
        # If the form has been submitted...
        # A form bound to the POST data

    #return render_to_response('events.html', {},
    #                          context_instance=RequestContext(request))

def events(request):
    """ Event page
    """
    print "Event page %r" % request.method
    if request.method == 'POST':
        form = EventForm(request.POST)
        # A form bound to the POST data
        print "Process the form"
        if form.is_valid():
            print("Form is valid")
            created_date = form.data.get('created_date')
            if created_date:
                created_date = datetime.datetime.strptime(created_date, '%Y/%m/%d')
            else:
                created_date = None

            event = Event(title=form.data.get('title'), created_date=created_date,
                          description=form.data.get("description"), location=form.data.get("location"))
            event.save()

    # reload event page
    form = EventForm()
    return render_to_response('events.html', {'form': form},
                              context_instance=RequestContext(request))


def event_detail(request, id):
    """ Return a JSON dict mapping for event given id
    """
    event = get_object_or_404(Event, pk=id)
    event_dict = {
        "success": 1,
        "result": [{
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "created_date": event.created_date.strftime('%Y/%m/%d'),
            "location": event.location
        }]
    }

    return HttpResponse(json.dumps(event_dict),
                        content_type="application/json")


def event_list(request, *args):
    """ Event data
    """
    print "Event list %r" % request.method
    event_obj = Event.objects.all()
    event_data = []
    for event in event_obj:
        time_mili = utils.unix_time_millis(event.created_date.replace(tzinfo=None))
        event_dict = {
        "id": event.id,
        "title": event.title,
        "url": "#",
        "class": "event-special",
        "start": time_mili,
        "end": time_mili
        }
        event_data.append(event_dict)

    event_list_data = {
    "success": 1,
    "result": event_data}

    print event_list_data

    return HttpResponse(json.dumps(event_list_data), content_type="application/json")


def task_list_create(request):
    """ Create new list
    """
    if request.method == 'POST':
        # If the form has been submitted...
        form = TaskListForm(request.POST)
        # A form bound to the POST data
        print "Process the form"
        if form.is_valid():
            print("Form is valid")

            t = TaskList(title=form.data.get('title'))
            t.save()
            return HttpResponseRedirect(reverse('todo.views.task_list'))
        print "Form is invalid"
        print form._errors
    else:
        # An unbound form
        form = TaskListForm()
    return render_to_response('new_list.html', {'form': form},
                              context_instance=RequestContext(request))


def task_create(request):
    """ Create new task view
    """
    if request.method == 'POST':
        # If the form has been submitted...
        form = TaskForm(request.POST)
        # A form bound to the POST data
        print "Process the form"
        if form.is_valid():
            print("Form is valid")
            # All validation rules pass
            # Process the data in form.cleaned_data
            start_date = form.data.get('start_date')
            print start_date
            if start_date:
                start_date = datetime.datetime.strptime(start_date, '%d/%M/%Y')
            else:
                start_date = None
            due_date = form.data.get('due_date')
            if due_date:
                due_date = datetime.datetime.strptime(due_date, '%d/%m/%Y')
            else:
                due_date = None

            completed = form.data.get('completed')
            if not completed:
                completed = False

            t = Task(title=form.data.get('title'), start_date=start_date,
                     due_date=due_date, completed=completed,
                     todo_list_id=form.data.get('todo_list'),
                     priority=form.data.get('priority'))
            t.save()
            return HttpResponseRedirect(reverse('todo.views.task_list'))
        print "Form is invalid"
    else:
        # An unbound form
        form = TaskForm()
    return render_to_response('new_task.html', {'form': form},
                              context_instance=RequestContext(request))


def contact_us(request):
    """ DIsplay input form for sending message.
    """
    return render_to_response('contact.html', {},
                              context_instance=RequestContext(request))

