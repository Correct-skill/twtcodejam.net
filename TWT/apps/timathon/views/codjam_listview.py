"""
This has not been completed
This is for past codejams and showing the leaderboard
"""
from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from ...challenges.models.challenge import Challenge
from ..models.team import Team
from ..models.submission import Submission
from TWT.context import get_discord_context


class PreviousView(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest) -> HttpResponse:
        context: dict = self.get_context(request=request)
        if not context["is_verified"]:
            messages.add_message(request, messages.WARNING, "You are not in the server")
            return redirect('/')
        challenge_list = []
        challenges = Challenge.objects.filter(ended=True, posted=True, type='MO')
        for challenge in challenges:
            # teams = Team.objects.filter(challenge=challenge, submitted=True).exclude(winner=0)
            submissions = Submission.objects.filter(
                team__in=Team.objects.filter(challenge=challenge, submitted=True).exclude(winner=0)
                )
            challenge_list.append({'challenge': challenge, 'submissions': submissions})
        context['challenge_list'] = challenge_list
        # print(context)
        return render(request,'timathon/codejam_listView.html',context)
