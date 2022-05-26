from rest_framework import serializers
from todo.models import Todo 

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['user_id', 'todo_id','title','content','is_deleted','modified_at','create_at']