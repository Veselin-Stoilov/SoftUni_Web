from django.urls import path

from SoftUni_Web.tasks.views import home, user

urlpatterns = (
    path('', home),
    path('user', user),
)
