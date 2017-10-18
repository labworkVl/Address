from main import views, apiView
from django.conf.urls import include
from main.models import *
"""ttmmpp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from rest_framework import serializers, viewsets, routers


#class StreetSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = Street
#        fields = ('name',)


#class StreetViewSet(viewsets.ModelViewSet):
#    queryset = Street.objects.all()
#    serializer_class = StreetSerializer

#router = routers.DefaultRouter()
#router.register(r'streets/', StreetViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),


    #url(r'^streets/$', views.streets_list),
    #url(r'^streets_all/$', views.streets_all),
    #url(r'^streets_class_all/$', apiView.StreetList.as_view()),
    url(r'^streets/$', apiView.StreetsList.as_view()),
    url(r'^streets/(?P<pk>[0-9]+)/$', apiView.StreetDetail.as_view()),
    url(r'^doma/$', apiView.DomaList.as_view()),
    url(r'^doma/(?P<ds>[0-9]+)/$', apiView.DomaListStreet.as_view()),

    url(r'^data/', views.return_data, name='data'),
    #    url(r'^/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
