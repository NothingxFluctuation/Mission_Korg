from django.conf.urls import url
from .views import get_file, send_code

urlpatterns = [
    url(r'^$',get_file,name='get_file'),
    
]
