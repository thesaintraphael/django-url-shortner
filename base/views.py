from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Link
from .serializers import LinkSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def generate_url(request):
    serializer = LinkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response({"error": 'Enter valid url'})


def redirect_url(request, code):

    link = get_object_or_404(Link, code=code)
    return redirect(link.url)
