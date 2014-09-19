from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from todo.api import TodoItemResource

v1_api = Api(api_name='v1')
v1_api.register(TodoItemResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'todo.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
)
