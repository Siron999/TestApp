from django.shortcuts import render
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
import boto3


@api_view(['GET', 'POST'])
def index(request, id):
    if request.method == 'GET':
        print("API Called")
        try:
            # fetch filename from db
            file = File.objects.get(id=id)

            if file is not None:
                print("file found", file.filename)
                s3 = boto3.client('s3')
                bucket_name = 'siron-bucket'
                key = file.filename

                response = s3.get_object(Bucket=bucket_name, Key=key)
                content_type = response['ContentType']
                data_bytes = response['Body']
                print(content_type)
                response = FileResponse(
                    data_bytes,
                    content_type=content_type
                )
                return response
            else:
                return Response("File not found in DB", status=404)
        except Exception as e:
            return Response(f"Error fetching document: {e}", status=500)
