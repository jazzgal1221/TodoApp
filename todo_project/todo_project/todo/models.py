from django.db import models
from django.contrib.auth.models import User
import datetime


PRIORITY_CHOICES = (

  (1, 'Low'),

  (2, 'Normal'),

  (3, 'High'),

)


class TaskList(models.Model):
    """ A list of items to do
    """

    title = models.CharField(max_length=250)
    creator = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        """ Representation string
        """
        output = self.title
        if self.creator:
            output += " - " + self.creator
        return output

    def num_tasks(self):
        """ Return list number of item
        """
        return self.task_set.count()

    def num_tasks_completed(self):
        """ Return number of completed items.
        """
        return self.task_set.filter(completed=True).count()

    def percent_completed(self):
        """ Return percentage of complete item
        """
        if self.num_tasks() == 0:
            return 0
        return int(float(self.num_tasks_completed()) / self.num_tasks() * 100)

    def tasks(self):
        return [task.__dict__ for task in self.task_set.all()]

    class Meta:
        """ Metadata for db model
        """
        ordering = ['title']


class Event(models.Model):
    """ An event represent
    """

    title = models.CharField(max_length=100, blank=True, null=True)

    created_date = models.DateTimeField(default=datetime.datetime.now, blank=True, null=True)

    description = models.TextField(max_length=5000, blank=True, null=True)

    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """ Object representation
        """
        return self.title


class Task(models.Model):
    """ An item to do
    """

    title = models.CharField(max_length=250)

    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    completed = models.BooleanField(default=False)

    description = models.TextField(max_length=10000, blank=True, null=True)

    start_date = models.DateTimeField(default=datetime.datetime.now)

    due_date = models.DateTimeField(blank=True, null=True)

    todo_list = models.ForeignKey(TaskList)

    def __str__(self):
        """ Represent object by title
        """
        return self.title

    class Meta:
        """ Order by priority descending, title ascending
        """
        ordering = ['-priority', 'title']
