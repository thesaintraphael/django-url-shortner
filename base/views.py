from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


def index(request):
    return render(request, 'index.html')


@api_view
def generate_url(request):
    pass


def redirect_url(request, code):

    link = get_object_or_404(Link, code=code)
    return redirect(link.url)
