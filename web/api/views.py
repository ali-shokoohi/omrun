#rom rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token
from web.models import User, Employees, Clients, Projects, Plans, Tasks, ToDo, Photos, Comments, Likes, AllowPersons, Gallery, Purchases, Documents
from web.api.serializers import Projects_Serializers, Plans_Serializers, Employees_Serializers, Likes_Serializers, AllowPersons_Serializers, Purchases_serializers
from web.api.serializers import Tasks_Serializers, ToDo_serializers, User_Serializers, Photos_Serializers, Comments_Serializers, Gallery_Serializers, Documents_Serializers
from django.contrib.auth.hashers import check_password
from django.http import Http404
import json
#/=========================================================

#============================Views===========================

#View of api/ url
class index(APIView):
    def get(self, request, format=None):
        return Response(status=200, data={
            "status": "ok",
            "message": "Hello!"
        })

#View of api/login/ url
class login(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    def post(self, request, format=None):
        user = request.user
        employee = Employees.objects.get(user=user)
        token = Token.objects.get(user=user)
        serializer = Employees_Serializers(employee)
        result = {
            "status": "ok",
            "employee": serializer.data,
            "token": token.key
        }
        return Response(status=200, data=result)

class Employees_list(APIView):
    def get(self, request, format=None):
        all_employees = Employees.objects.all()
        serializer = Employees_Serializers(all_employees, many=True)
        return Response(status=200, data={
            "status": "ok",
            "projects": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        user_data = data["user"]
        user_serializer = User_Serializers(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            serializer = Employees_Serializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=201, data={
                    "status": "ok",
                    "project": serializer.data
                })
            return Response(status=400, data={
                "status": "bad",
                "error": serializer.errors
            })
        return Response(status=400, data={
            "status": "bad",
            "error": user_serializer.errors
        })



#View of api/projects/ url
class projects_list(APIView):
    def get(self, request, format=None):
        all_projects = Projects.objects.all()
        serializer = Projects_Serializers(all_projects, many=True)
        return Response(status=200, data={
            "status": "ok",
            "projects": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Projects_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "project": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/projects/<int:pk>/ url
class projects_detial(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Projects.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = Projects_Serializers(project)
        return Response(status=200, data={
            "status": "ok",
            "projects": serializer.data
        })
    def put(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = Projects_Serializers(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "project": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/plans/ url
class plans_list(APIView):
    def get_project(self):
        try:
            return self.request.GET["project"]
        except:
            raise Http404
    def get_object(self, p_id):
        try:
            project = Projects.objects.get(id=p_id)
            return Plans.objects.filter(project=project)
        except Plans.DoesNotExist:
            raise Http404
        except Projects.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        project_id = self.get_project()
        the_plans = self.get_object(project_id)
        serializer = Plans_Serializers(the_plans, many=True)
        return Response(status=200, data={
            "status": "ok",
            "plans": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Plans_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "plan": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/plans/<int:pk>/ url
class plans_detail(APIView):
    def get_object(self, pk):
        try:
            return Plans.objects.get(pk=pk)
        except Plans.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        plan = self.get_object(pk)
        serializer = Plans_Serializers(plan)
        return Response(status=200, data={
            "status": "ok",
            "plans": serializer.data
        })
    def put(self, request, pk, format=None):
        plan = self.get_object(pk)
        serializer = Plans_Serializers(plan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "plan": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        plan = self.get_object(pk)
        plan.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/plans/ url
class Allow_list(APIView):
    def get_project(self):
        try:
            return self.request.GET["project"]
        except:
            raise Http404
    def get_object(self, p_id):
        try:
            project = Projects.objects.get(id=p_id)
            return AllowPersons.objects.filter(project=project)
        except AllowPersons.DoesNotExist:
            raise Http404
        except Projects.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        project_id = self.get_project()
        persons = self.get_object(project_id)
        serializer = AllowPersons_Serializers(persons, many=True)
        return Response(status=200, data={
            "status": "ok",
            "persons": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = AllowPersons_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "person": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/plans/<int:pk>/ url
class Allow_detail(APIView):
    def get_object(self, pk):
        try:
            return AllowPersons.objects.get(pk=pk)
        except AllowPersons.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = AllowPersons_Serializers(person)
        return Response(status=200, data={
            "status": "ok",
            "persons": serializer.data
        })
    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = AllowPersons_Serializers(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "person": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/tasks/ url
class Tasks_list(APIView):
    def get(self, request, format=None):
        all_tasks = Tasks.objects.all()
        serializer = Tasks_Serializers(all_tasks, many=True)
        return Response(status=200, data={
            "status": "ok",
            "tasks": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Tasks_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "tasks": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
#View of api/tasks/<int:pk>/ url
class Tasks_detial(APIView):
    def get_object(self, pk):
        try:
            return Tasks.objects.get(pk=pk)
        except Tasks.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = Tasks_Serializers(task)
        return Response(status=200, data={
            "status": "ok",
            "tasks": serializer.data
        })
    def put(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = Tasks_Serializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "task": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/todo/ url
class ToDo_list(APIView):
    def get_tasks(self):
        try:
            return self.request.GET["task"]
        except:
            raise Http404
    def get_object(self, p_id):
        try:
            task = Tasks.objects.get(id=p_id)
            return ToDo.objects.filter(task=task)
        except ToDo.DoesNotExist:
            raise Http404
        except Tasks.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        task_id = self.get_tasks()
        the_todo = self.get_object(task_id)
        serializer = ToDo_serializers(the_todo, many=True)
        return Response(status=200, data={
            "status": "ok",
            "todos": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = ToDo_serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "todo": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/todo/<int:pk>/ url
class ToDo_detail(APIView):
    def get_object(self, pk):
        try:
            return ToDo.objects.get(pk=pk)
        except ToDo.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDo_serializers(todo)
        return Response(status=200, data={
            "status": "ok",
            "todo": serializer.data
        })
    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = ToDo_serializers(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "todo": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/gallerys/ url
class Gallery_list(APIView):
    def get(self, request, format=None):
        all_Gallerys = Gallery.objects.all()
        serializer = Gallery_Serializers(all_Gallerys, many=True)
        return Response(status=200, data={
            "status": "ok",
            "gallerys": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Gallery_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "Galerys": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/gallerys/<int:pk>/ url
class Gallery_detial(APIView):
    def get_object(self, pk):
        try:
            return Gallery.objects.get(pk=pk)
        except Gallery.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = Gallery_Serializers(gallery)
        return Response(status=200, data={
            "status": "ok",
            "Galerry": serializer.data
        })
    def put(self, request, pk, format=None):
        gallery = self.get_object(pk)
        serializer = Gallery_Serializers(gallery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "gallery": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        gallery = self.get_object(pk)
        gallery.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/photos/ url
class Photos_list(APIView):
    def get(self, request, format=None):
        all_photos = Photos.objects.all()
        serializer = Photos_Serializers(all_photos, many=True)
        return Response(status=200, data={
            "status": "ok",
            "photos": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Photos_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "photos": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/photos/<int:pk>/ url
class Photos_detial(APIView):
    def get_object(self, pk):
        try:
            return Photos.objects.get(pk=pk)
        except Photos.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = Photos_Serializers(photo)
        return Response(status=200, data={
            "status": "ok",
            "photos": serializer.data
        })
    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = Photos_Serializers(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "photo": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/likes/ url
class Likes_list(APIView):
    def get_photos(self):
        try:
            return self.request.GET["photo"]
        except:
            raise Http404
    def get_object(self, p_id):
        try:
            photo = Photos.objects.get(id=p_id)
            return Likes.objects.filter(image=photo)
        except Likes.DoesNotExist:
            raise Http404
        except Photos.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        photo_id = self.get_photos()
        the_likes = self.get_object(photo_id)
        serializer = Likes_Serializers(the_likes, many=True)
        return Response(status=200, data={
            "status": "ok",
            "likes": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Likes_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "like": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/likes/<int:pk>/ url
class Likes_detail(APIView):
    def get_object(self, pk):
        try:
            return Likes.objects.get(pk=pk)
        except Likes.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        like = self.get_object(pk)
        serializer = Likes_Serializers(like)
        return Response(status=200, data={
            "status": "ok",
            "like": serializer.data
        })
    def put(self, request, pk, format=None):
        like = self.get_object(pk)
        serializer = Likes_Serializers(like, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "like": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        like = self.get_object(pk)
        like.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/comments/ url
class Comments_list(APIView):
    def get_photos(self):
        try:
            return self.request.GET["photo"]
        except:
            raise Http404
    def get_object(self, p_id):
        try:
            photo = Photos.objects.get(id=p_id)
            return Comments.objects.filter(image=photo)
        except Comments.DoesNotExist:
            raise Http404
        except Photos.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        photo_id = self.get_photos()
        the_comments = self.get_object(photo_id)
        serializer = Comments_Serializers(the_comments, many=True)
        return Response(status=200, data={
            "status": "ok",
            "comments": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Comments_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "comment": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/comments/<int:pk>/ url
class Comments_detail(APIView):
    def get_object(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except Comments.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = Comments_Serializers(comment)
        return Response(status=200, data={
            "status": "ok",
            "comment": serializer.data
        })
    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = Comments_Serializers(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "comment": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/trakonesh/ url
class Purchases_list(APIView):
    def get(self, request, format=None):
        all_Purchases = Purchases.objects.all()
        serializer = Purchases_serializers(all_Purchases, many=True)
        return Response(status=200, data={
            "status": "ok",
            "purchases": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Purchases_serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "purchases": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/photos/<int:pk>/ url
class Purchases_detial(APIView):
    def get_object(self, pk):
        try:
            return Purchases.objects.get(pk=pk)
        except Purchases.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        purchase = self.get_object(pk)
        serializer = Purchases_serializers(purchase)
        return Response(status=200, data={
            "status": "ok",
            "purchases": serializer.data
        })
    def put(self, request, pk, format=None):
        purchase = self.get_object(pk)
        serializer = Purchases_serializers(purchase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "purchase": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        purchase = self.get_object(pk)
        purchase.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#View of api/documents/ url
class Documents_list(APIView):
    def get(self, request, format=None):
        all_Documents = Documents.objects.all()
        serializer = Documents_Serializers(all_Documents, many=True)
        return Response(status=200, data={
            "status": "ok",
            "documents": serializer.data
        })
    def post(self, request, format=None):
        data = request.data
        serializer = Documents_Serializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data={
                "status": "ok",
                "documents": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })

#View of api/photos/<int:pk>/ url
class Documents_detial(APIView):
    def get_object(self, pk):
        try:
            return Documents.objects.get(pk=pk)
        except Documents.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = Documents_Serializers(document)
        return Response(status=200, data={
            "status": "ok",
            "documents": serializer.data
        })
    def put(self, request, pk, format=None):
        document = self.get_object(pk)
        serializer = Documents_Serializers(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200, data={
                "status": "ok",
                "document": serializer.data
            })
        return Response(status=400, data={
            "status": "bad",
            "error": serializer.errors
        })
    def delete(self, request, pk, format=None):
        document = self.get_object(pk)
        document.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

#Just for fucking andriod idiot
#///////////////////////////////////////////////
def logging(username, password):
    if True:
        return True
    else:
        return Http404
class Plan_delete(APIView):
    def get_object(self, pk):
        try:
            return Plans.objects.get(pk=pk)
        except Plans.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        plan = self.get_object(pk)
        plan.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })

class Project_delete(APIView):
    def get_object(self, pk):
        try:
            return Projects.objects.get(pk=pk)
        except Plans.DoesNotExist:
            raise Http404
    def post(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=201, data={
            "status": "ok",
            "message": "Deleted"
        })
#///////////////////////////////////////////////