from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('predict/', views.home, name='predict'),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="predictor/login.html"
        ),
        name="login"
    ),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path(
        "history/",
        views.prediction_history,
        name="history"
    ),

    path("analytics/", views.analytics, name="analytics"),
]
