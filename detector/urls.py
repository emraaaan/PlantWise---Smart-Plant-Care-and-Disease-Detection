from django.urls import path
from . import views

app_name = "detector"

urlpatterns = [
    path("diagnose/", views.diagnose_plant, name="diagnose"),
    path("result/<int:pk>/", views.diagnosis_result, name="diagnosis_result"),
    path("history/", views.history, name="history"),
    path("upload/", views.diagnose_plant, name="upload"),
]
