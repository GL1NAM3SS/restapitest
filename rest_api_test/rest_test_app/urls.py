from django.urls import path
from .views import TopicView

app_name = "rest_test_app"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('topics/', TopicView.as_view()),
    path('topics/<int:pk>', TopicView.as_view())
]