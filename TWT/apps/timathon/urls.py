from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "timathon"
urlpatterns = [
    path("", views.home, name="Home"),
    path("newteam/", views.create_team, name="Create_Team"),
    path("team/<int:team_ID>/", views.view_teams, name="ViewTeams"),
    path("submit/", views.submission, name="Submission"),
    path("member/<str:invite>", views.add_member, name="Add_member"),
    path("leave/", views.leave_team, name="LeaveTeam"),
    path("submissionlist/", views.submission_list, name="submissionList"),
    path("history/", views.past_view, name="History"),
    # Judging
    path("judge/", login_required(views.judge), name="Judge"),
    path(
        "judge/vote/<int:submission_id>/",
        login_required(views.judge_vote),
        name="JudgeVote",
    ),
]
