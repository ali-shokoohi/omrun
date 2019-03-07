from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from web.models import Employees
from hashlib import md5
#/=========================================================

#Check authentication of login request
def logging(username, password):
    try:
        user_check = Employees.objects.filter(personnelـid=username).exists()
        if user_check is True:
            user = Employees.objects.filter(personnelـid=username).get()
            pass_hash = md5(password.encode("utf-8")).hexdigest()
            if user.password == pass_hash:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

#============================Views===========================

#View of api/ url
@api_view(['post'])
@parser_classes((JSONParser,))
def index(request, format=None):
    return Response(status=200, data={
        "status": "ok",
        "message": "Hello"
    })

#View of api/login/ url
@api_view(['post'])
@parser_classes((JSONParser,))
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def login(request, format=None):
    #Request should have "username" and "password" params
    if "username" in request.data and "password" in request.data:
        username = request.data["username"]
        password = request.data["password"]
        status = 200
        #Check authentication of request
        if logging(username, password) is True:
            #Send user's information
            user = Employees.objects.filter(personnelـid=username).get()
            result = {
                "status": "ok",
                "information": {
                    "name": user.name,
                    "post": user.post,
                    "personnelـid": user.personnelـid,
                    "email": user.email,
                    "profile_pic": user.profile_pic
                }
            }
        else:
            status = 403
            result = {
                "status": "bad",
                "error": "Username or password was incorrent"
            }
    else:
        status = 405
        result = {
            "status": "bad",
            "error": "Send all params"
        }
    return Response(status=status, data=result)