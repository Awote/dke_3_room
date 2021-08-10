from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import request
import os
from django.core.files import File
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from rest_framework.views import APIView
from .serialization import *
from django.shortcuts import get_object_or_404, render
# from .models import *
def index(request):
    return render(request, 'HTML\index.html')
# def count_client(request):
#     return Resp()