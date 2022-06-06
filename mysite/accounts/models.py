from django.urls import path

from django.db import models

# Create your models here.
from aplicatie1.views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
]