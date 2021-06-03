from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import Challenge
from TWT.context import get_discord_context
from TWT.discord import client


class StopSubmission(View):
    def get_context(self, request: WSGIRequest) -> dict:
        return get_discord_context(request=request)

    def get(self, request: WSGIRequest, challenge_id: int):
        if not request.user.is_authenticated:
            messages.add_message(request, messages.INFO, "You are not logged in!")
            return redirect("/")

        context = self.get_context(request=request)
        if not context["is_verified"]:
            return redirect("/")
        if context["is_admin"] or context["is_challenge_host"]:
            challenge = get_object_or_404(
                Challenge, id=challenge_id
            )  # Challenge.objects.get(id=challenge_id)
            challenge.submissions_status = False
            challenge.save()
            messages.add_message(
                request, messages.INFO, "Submissions Have been stopped"
            )
            client.send_webhook(
                "Timathon",
                f"Submissions for the Timathon have been stopped",
                fields=[
                    {
                        "name": "Link",
                        "value": f"[Visit]({request.build_absolute_uri('/timathon/')})",
                    }
                ],
                codeJamInfo=True,
            )
            client.send_webhook(
                "Code Jam",
                f"<@{context['discord_user'].uid}> has stopped accepting submissions for the code jam",
                fields=[
                    {
                        "name": "Link",
                        "value": f"[Visit]({request.build_absolute_uri('/timathon/')})",
                    }
                ],
            )
            return redirect("timathon:Home")
