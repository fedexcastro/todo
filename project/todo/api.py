from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.paginator import Paginator

from todo.models import TodoItem


class TodoItemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'item'
        excludes = ['created_datetime', 'last_edit_datetime', 'user']

        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()

        paginator = Paginator

    def hydrate(self, bundle):
        if bundle.request.user.is_authenticated():
            user = bundle.request.user
        else:
            bundle.errors

        bundle.obj.user = user
        return bundle

    def dehydrate(self, bundle):
        bundle.data['username'] = bundle.obj.user.username
        return bundle

    def get_object_list(self, request):
        return super(TodoItemResource, self).get_object_list(request).filter(user=request.user)
        
# from tastypie.authorization import Authorization


# class AuthorizationLimits(Authorization):
#
#     def read_list(self, object_list, bundle):
#         return object_list.filter(user__id=bundle.request.user.id)