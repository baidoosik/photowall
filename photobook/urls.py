from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.home, name='ameria_home'),
    url(r'^lover/$',views.lover, name='lover'),

]