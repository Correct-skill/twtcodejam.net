"""sylte_xyz URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from importlib import import_module

from django.contrib import admin
from django.urls import path, include

from allauth.socialaccount import providers
from TWT.views import handler404, handler500

handler404 = handler404
handler500 = handler500

# def trigger_error(request):
#   division_by_zero = 1 / 0


urlpatterns = [
    path("", include("TWT.apps.challenges.urls", namespace="home")),
    path("admin/", admin.site.urls),
    path("timathon/", include("TWT.apps.timathon.urls", namespace="timathon")),
    # path('weekly/', include('TWT.apps.weekly.urls', namespace="weekly")),
    path("martor/", include("martor.urls")),
    # path('sentry-debug/', trigger_error),
]

# For discord login.

provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns
