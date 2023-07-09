from todos.models import Todo
from django_filters import rest_framework as filters

class TodoFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields = ['checked']
    
