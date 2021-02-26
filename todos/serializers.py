from .models import Todo, Comment
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name = 'comment-detail', read_only = True)
    class Meta:
        model = Todo
        fields = ['url', 'id', 'title', 'description', 'is_completed', 'created_at', 'updated_at', 'comments']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    todo_id = serializers.ReadOnlyField(source='todo.id')
    class Meta:
        model = Comment
        fields = ['url', 'id', 'todo_id', 'contents', 'created_at', 'updated_at']