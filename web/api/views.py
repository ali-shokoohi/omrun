#rom rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from web.models import User, Employees, Clients, Projects, Plans
from web.api.serializers import Projects_Serializers, PLans_Serializers, Employees_Serializers
from django.contrib.auth.hashers import check_password
from django.http import Http404
import json
#/=========================================================

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
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        user = request.user
        employee = Employees.objects.get(user=user)
        serializer = Employees_Serializers(employee)
        result = {
            "status": "ok",
            "information":serializer.data
        }
        return Response(status=200, data=result)

#View of api/projects/ url
class projects(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            return Http404
    def post(self, request, format=None):
        all_projects = Projects.objects.all()
        serializer = Projects_Serializers(all_projects, many=True)
        return Response(status=200, data={
            "status": "ok",
            "projects": serializer.data
        })
    def delete(self, request, format=None):
        project = self.get_object(pk)
        project.delete()

#View of api/plans/ url
class plans(APIView):
    def get_object(self, pk):
        try:
            return Plans.objects.get(pk=pk)
        except Plans.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = PLans_Serializers(project)
        return Response(status=200, data=serializer.data)
