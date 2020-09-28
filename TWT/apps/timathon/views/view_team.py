from allauth.socialaccount.models import SocialAccount
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from TWT.apps.challenges.models import Challenge
from TWT.apps.timathon.models import Team
from TWT.context import get_discord_context


class View_teams(View):
    def get_context(self, request: WSGIRequest, team_ID) -> dict:
        context = get_discord_context(request)


        team = Team.objects.get(ID=team_ID)

        members = team.members.all()
        discord_members = []
        for member in members:
            new_member = {}
            try:
                user = SocialAccount.objects.get(user_id=member.id)
            except SocialAccount.DoesNotExist:
                pass
            else:
                new_member["user_id"] = user.uid
                new_member["avatar_url"] = user.get_avatar_url()
                new_member["username"] = user.extra_data["username"]
                new_member["discriminator"] = user.extra_data["discriminator"]
            discord_members.append(new_member)
        team.discord_members = discord_members
        print(team)
        context['team'] = team
        context['invite'] = request.build_absolute_uri(location=f"/timathon/member/{team.invite}")
        return context

    def get(self, request: WSGIRequest, team_ID) -> HttpResponse:
        if not request.user.is_authenticated:
            return redirect('/')
        context = self.get_context(request=request, team_ID=team_ID)

        return render(
            request=request,
            template_name="timathon/view_team.html",
            context=context
        )