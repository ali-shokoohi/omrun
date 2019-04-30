#rom rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from web.models import User, Employees, Clients, Projects, Plans
from web.api.serializers import Projects_Serializers, PLans_Serializers
from django.contrib.auth.hashers import check_password
from django.http import Http404
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
class index(APIView):
    def post(self, request, format=None):
        return Response(status=200, data={
            "status": "ok",
            "message": "Hello!"
        })

#View of api/login/ url
class login(APIView):
    def post(self, request, format=None):
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

#View of api/projects/ url
class projects(APIView):
    def post(self, request, format=None):
        all_projects = Projects.objects.all()
        serializer = Projects_Serializers(all_projects, many=True)
        return Response(status=200, data={
            "status": "ok",
            "projects": serializer.data
        })

#View of api/plans/ url
class plans(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = PLans_Serializers(project)
        return Response(status=200, data=serializer)
