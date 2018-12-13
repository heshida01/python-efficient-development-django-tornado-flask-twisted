from django.conf.urls import url
from app.admin import admin_site

from . import views

urlpatterns = [
    url(r'moments_input', views.moments_input),
    url(r'', views.welcome),
    url(r'^myadmin/', admin_site.urls),
]
