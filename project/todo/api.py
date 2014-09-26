from tastypie_oauth.authentication import OAuth20Authentication
from tastypie.authentication import SessionAuthentication, MultiAuthentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.paginator import Paginator

from todo.models import TodoItem
from todouser.models import User


class MyAuthentication(SessionAuthentication):
    def is_authenticated(self, request, **kwargs):
        return request.user.is_authenticated()


class MyModelResource(ModelResource):

    def wrap_view(self, view):
        super(MyModelResource, self).wrap_view(view)


class TodoItemResource(ModelResource):
    class Meta:
        queryset = TodoItem.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'item'
        excludes = ['created_datetime', 'last_edit_datetime', 'user']

        authorization = Authorization()
        authentication = MultiAuthentication(SessionAuthentication(), OAuth20Authentication())

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
        return super(TodoItemResource, self).get_object_list(request).filter(user__username=request.user.username).order_by('priority')


class TodoUserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        allowed_methods = ['get', 'put']
        resource_name = 'user'
        excludes = ['password', 'is_staff', 'is_superuser']

        authorization = DjangoAuthorization()
        authentication = MultiAuthentication(OAuth20Authentication(), SessionAuthentication())

    def dehydrate(self, bundle):
        clients = [{'name': ak.name,
                    'url': ak.url,
                    'client_id': ak.client_id,
                    'client_secret': ak.client_secret} for ak in bundle.obj.oauth2_client.all()]

        bundle.data['clients'] = clients
        return bundle

    def get_object_list(self, request):
        return super(TodoUserResource, self).get_object_list(request).filter(username=request.user.username)


