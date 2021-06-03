from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from TWT.discord import client
from ..models.team import Team
from TWT.context import get_discord_context
from django import forms
from ...challenges.models.challenge import Challenge
from django.contrib import messages


class LeaveTeam(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest):
        if not request.user.is_authenticated:
            return redirect("/")
        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect("/")
        user = request.user
        challenge = get_object_or_404(
            Challenge, ended=False, posted=True, type="MO"
        )  # Challenge.objects.get(ended=False, posted=True, type='MO')
        if len(Team.objects.filter(challenge=challenge, members=user)) <= 0:
            messages.add_message(request, messages.WARNING, "You are not in a team !")
            client.send_webhook(
                "Teams",
                f"<@{context['discord_user'].uid}> tried leaving his team",
                [{"name": "error", "value": "They are not in a team"}],
            )
            return redirect("timathon:Home")
        team = get_object_or_404(
            Team, challenge=challenge, members=user
        )  # Team.objects.get(challenge=challenge, members=user)
        team.members.remove(user)
        team.save()
        if len(team.members.all()) == 0:
            team.delete()
        messages.add_message(request, messages.INFO, "Removed you from the team!")
        client.send_webhook(
            "Teams",
            f"<@{context['discord_user'].uid}> left his team",
        )
        return redirect("timathon:Home")
