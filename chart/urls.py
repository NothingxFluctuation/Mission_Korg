from django.conf.urls import url
from .views import show_data

urlpatterns = [
    url(r'^$',show_data, name='show_data'),

]
