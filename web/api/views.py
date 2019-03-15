from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from web.models import User, Employees, Clients, Projects
from django.contrib.auth.hashers import check_password
#/=========================================================

#Check authentication of login request
def logging(username, password):
    try:
        user_check = User.objects.filter(username=username).exists()
        if user_check is True:
            user = User.objects.get(username=username)
            pass_check = check_password(password, user.password)
            if pass_check is True:
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
    #Get prjects informations
    projects = Projects.objects.all()
    project_list = list()
    for project in projects:
        projects_dict = dict()
        projects_dict["id"] = project.id
        projects_dict["name"] = project.name
        projects_dict["employer"] = project.employer.user.first_name
        project_list.append(projects_dict)
    return Response(status=200, data={
        "status": "ok",
        "message": "Hello",
        "projects": project_list
    })

#View of api/login/ url
@api_view(['post'])
@parser_classes((JSONParser,))
def login(request, format=None):
    #Request should have "username" and "password" params
    if "username" in request.data and "password" in request.data:
        username = request.data["username"]
        password = request.data["password"]
        status = 200
        #Check authentication of request
        if logging(username, password) is True:
            #Send user's information
            user = User.objects.get(username=username)
            name = user.first_name+' '+user.last_name
            employee = Employees.objects.get(user=user)
            token = Token.objects.get(user=user)
            result = {
                "status": "ok",
                "information": {
                    "name": name,
                    "post": employee.post,
                    "personnelـid": user.username,
                    "email": user.email,
                    "profile_pic": employee.profile_pic,
                    "token": token.key
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

#Where Token is neccesarry
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
#def ...: