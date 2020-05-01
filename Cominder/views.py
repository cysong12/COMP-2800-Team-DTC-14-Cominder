from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators

@require_GET
def home(request):
    return HttpResponse("<h1>Home Page</h1>")