from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.home, name='lover'),
    url(r'^global_challenge/$',views.global_challenge, name='global_challenge'),
    url(r'^indonesia/$',views.indonesia, name='indonesia'),
    url(r'^mwc/$',views.mwc, name='mwc'),

]