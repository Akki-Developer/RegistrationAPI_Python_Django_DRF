from django.conf.urls import url
from Regi_api import views

urlpatterns = [
    url(r'form', views.SnippetList.as_view(), name='Formview'),
]