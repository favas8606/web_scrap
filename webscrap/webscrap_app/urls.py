from .  import views
from django.urls import path
app_name = "webscrap_app"
urlpatterns = [
    path('',views.home, name="home"),
    path('clear', views.clear, name="clear")
]