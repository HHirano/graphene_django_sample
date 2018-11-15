from django.conf.urls import include, url
from django.contrib import admin
from graphene_django.views import GraphQLView


urlpatterns = [
    url(r'^graphql/', GraphQLView.as_view(graphiql=True)),
    url(r'^admin/', admin.site.urls),
]


from channels.routing import route_class
from graphql_ws.django_channels import GraphQLSubscriptionConsumer


channel_routing = [
    route_class(GraphQLSubscriptionConsumer, path=r'^/subscriptions'),
]
