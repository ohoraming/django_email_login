from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from todo.models import Todo
from todo.serializers import TodoSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

@csrf_exempt
def todo_list(request):
    """
    todo 전체를 조회하거나 신규 todo를 생성하는 역할
    """
    if request.method == 'GET': # 전체 조회
        query_set = Todo.objects.all() # 모든 객체 읽기
        serializer = TodoSerializer(query_set, many=True) # 모든 객체를 serializer에 넣으면 Json형태로 반환
        return JsonResponse(serializer.data, safe=False) # 항상 Response 형태로 반환해야 함(HttpResponse/JsonResponse)
    
    elif request.method == 'POST': # 신규 생성
        print(request)
        """
        <WSGIRequest: POST '/todo/'>
        """
        data = JSONParser().parse(request) # JSON으로 온 데이터를 parse함
        # print(data) 
        """
        {'title': "it's NINTH title", 'content': "it's NINTH content", 'is_deleted': False, 'user_id': 1}
        """
        serializer = TodoSerializer(data=data)
        # print(serializer)
        """
        TodoSerializer(data={'title': "it's NINTH title", 'content': "it's NINTH content", 'is_deleted': False, 'user_id': 1}):
            user_id = PrimaryKeyRelatedField(queryset=User.objects.all())
            todo_id = IntegerField(read_only=True)
            title = CharField(max_length=50)
            content = CharField(style={'base_template': 'textarea.html'})
            is_deleted = BooleanField(required=False)
            modified_at = DateTimeField(read_only=True)
            create_at = DateTimeField(read_only=True)
        """
        if serializer.is_valid(): # serializer의 model, field와 비교 후 일치하면, 
            serializer.save() # 객체 생성
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def todo(request, todo_id):
    """
    단건 조회, 수정, 삭제
    """
    
    obj = Todo.objects.get(todo_id=todo_id) # id 값으로 객체 하나를 불러옴
    # print(obj)
    """
    Todo object (15)
    """

    if request.method == 'GET': # read - 조회
        serializer = TodoSerializer(obj)
        # print(serializer)
        """
        TodoSerializer(<Todo: Todo object (15)>):
            user_id = PrimaryKeyRelatedField(queryset=User.objects.all())
            todo_id = IntegerField(read_only=True)
            title = CharField(max_length=50)
            content = CharField(style={'base_template': 'textarea.html'})
            is_deleted = BooleanField(required=False)
            modified_at = DateTimeField(read_only=True)
            create_at = DateTimeField(read_only=True)
        """
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'PUT': # update - 수정
        data = JSONParser().parse(request)
        serializer = TodoSerializer(obj, data=data) # 생성시에 썼던 구문과 같음
        # 수정이기때문에 serializer에 기존의 obj를 넣어준다는 점이 다름
        # print(serializer) 
        """
        TodoSerializer(<Todo: Todo object (15)>, data={'user_id': 1, 'todo_id': 15, 'title': "it's UPDATED SIXTH title", 'content': "it's UPDATED SIXTH content", 'is_deleted': False}):
            user_id = PrimaryKeyRelatedField(queryset=User.objects.all())
            todo_id = IntegerField(read_only=True)
            title = CharField(max_length=50)
            content = CharField(style={'base_template': 'textarea.html'})
            is_deleted = BooleanField(required=False)
            modified_at = DateTimeField(read_only=True)
            create_at = DateTimeField(read_only=True)
        """
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE': # delete - 삭제
        obj.delete()
        return HttpResponse(status=204)