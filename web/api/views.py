from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes

@api_view(['post'])
@parser_classes((JSONParser,))
def index(request, format=None):
    return Response(status=200, data={
        "status": "ok",
        "message": "Hello"
    })