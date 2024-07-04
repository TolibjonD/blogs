from django.urls import path
from .views import index, edit_form, logout

app_name="blogs"
urlpatterns = [
    path("", index, name="index"),
    path("logout/", logout, name="logout"),
    path("edit_form/<slug:slug>/", edit_form, name="edit_form")
]
