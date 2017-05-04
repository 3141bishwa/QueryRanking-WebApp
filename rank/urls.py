from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="rank/home.html")),
    url(r'^get_rank', views.get_rank, name='get_rank'),
]
