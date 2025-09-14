from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url='login/', permanent=False)),
    path("login/", views.login, name='login'),
    path("signup/", views.sign_up, name='sign_up'),
]