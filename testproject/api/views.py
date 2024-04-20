from django.shortcuts import render
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File


@api_view(['GET', 'POST'])
def index(request, id):
    if request.method == 'GET':
        print("API Called")
        try:
            # fetch filename from db
            file = File.objects.get(id=id)

            if file is not None:
                return Response({"filename": file.filename}, status=200)
            else:
                return Response("File not found in DB", status=404)
        except Exception as e:
            return Response(f"Error fetching document: {e}", status=500)
