from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from todo import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name="index"),
    url(r'tasks/new_task_list', 'todo.views.task_list_create', name="task_list_create"),
    url(r'tasks/new', 'todo.views.task_create', name="task_create"),
    url(r'tasks/delete/([0-9]+)/$', 'todo.views.task_delete', name="task_delete"),
    url(r'tasks/update/([0-9]+)/$', 'todo.views.task_update', name="task_update"),
    url(r'about', TemplateView.as_view(template_name='about.html'), name="about_page"),
    url(r'event_list', 'todo.views.event_list', name='event_list'),
    url(r'tasks', 'todo.views.task_list', name="tasks_page"),
    url(r'events', 'todo.views.events', name="events_page"),
    url(r'events/new', 'todo.views.create_event', name="event_create"),
    url(r'event_detail/([0-9]+)/$', 'todo.views.event_detail', name="event_detail"),
    url(r'contact', TemplateView.as_view(template_name='contact.html'), name="contact_page",),
    # Examples:
    # url(r'^$', 'todo_project.views.home', name='home'),
    # url(r'^todo_project/', include('todo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
