from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

app_name = "topics"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/answers/", views.results, name="results"),
    path("add_question/", views.add_question, name="add_question"),
    path('sign_up/', views.register, name='sign_up'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", views.custom_logout, name="logout"),
]