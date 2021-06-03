from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path(
        "",
        views.HomeView.as_view(),
        name="home",
    ),
    path("logout/", views.logout, name="logout"),
    path("new/", views.new, name="new"),
    path("delete/<int:challenge_id>", views.delete_view, name="delete"),
    #  path('view/<int:challenge_id>/', views.view, name="view"),
    path("start/<int:challenge_id>/", views.start, name="start"),
    path("end/<int:challenge_id>/", views.end, name="end"),
    path(
        "startsubmission/<int:challenge_id>",
        views.start_submission,
        name="StartSubmission",
    ),
    path(
        "stopsubmission/<int:challenge_id>",
        views.stop_submission,
        name="StopSubmissions",
    ),
    path("startteams/<int:challenge_id>", views.start_team, name="StartTeams"),
    path("stopteams/<int:challenge_id>", views.stop_team, name="StopTeams"),
    path("unreleased/", views.unreleased_view, name="unreleased"),
    path("startvoting/<int:challenge_id>", views.start_voting, name="StartVoting"),
    path("stopvoting/<int:challenge_id>", views.stop_voting, name="StopVoting"),
    path("pages/<str:link_name>", views.view_custom, name="custom view"),
]
