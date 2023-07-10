# from rest_framework import viewsets
# from todos.models import Todo
# from todos.serializers import TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


from todos.models import Todo
from todos.serializers import TodoSerializer
# from todos.serializers import TodoFilter
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics, viewsets


from django_filters import rest_framework as filters


from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend #new hmmmmm


class TodoList(mixins.CreateModelMixin, generics.GenericAPIView, mixins.ListModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
        
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # filterset_class = TodoFilter # for simple filtering
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if not request.data['value'].isspace():
            return self.create(request, *args, **kwargs)
        else:
            return print('data')
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def get_queryset(self):
        res = super().get_queryset()
        filter = self.request.query_params.get('filter')
        if filter == 'complited':
            return res.filter(checked=True)
        elif filter == 'active':
            return res.filter(checked=False)
        else:
            return res


        

    
    
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

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

class TodoDelete(generics.DestroyAPIView, generics.ListCreateAPIView,):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # filterset_class = TodoFilter

    

# class TodoChecked(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#     filter_backends = (DjangoFilterBackend)
#     list_filter = ["checked"]


# class TodoChecked(viewsets.ModelViewSet):
    # queryset = Todo.objects.all()

    # def get_queryset(self):
    #     res = super().get_queryset()
    #     checked = self.kwargs.get("checked")
    #     return res.filter(checked=True)
        
# class TodoChecked(generics.ListAPIView):
#     serializer_class = TodoSerializer


# class CheckedProductsList(generics.ListAPIView):

#     model = Todo
#     serializer_class = TodoSerializer
#     filterset_class = TodoFilter