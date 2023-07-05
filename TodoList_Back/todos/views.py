# from rest_framework import viewsets
# from todos.models import Todo
# from todos.serializers import TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


from todos.models import Todo
from todos.serializers import TodoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics


class TodoList(mixins.CreateModelMixin, generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin):
        
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TodoDetail(APIView):
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

class TodoDelete(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
