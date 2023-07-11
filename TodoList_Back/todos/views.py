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
from rest_framework.decorators import action
from rest_framework.request import Request




from django_filters import rest_framework as filters


from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend #new hmmmmm

from django.shortcuts import get_object_or_404


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
    

class TodoCheckedDelete(generics.DestroyAPIView):
    queryset = Todo.objects.filter(checked=True)
    serializer_class = TodoSerializer
    
    def delete(self, request, *args, **kwargs):
        todos = self.get_queryset()
        if todos.exists():
           todos.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_OK)


class TodoCheckedAll(generics.ListCreateAPIView):
    queryset = Todo.objects.filter(checked=False)
    serializer_class = TodoSerializer
    
    def post(self, request, *args, **kwargs):
        # update_todos = []
        todos = Todo.objects.filter(checked=False)
        for todo in todos:
            todo.checked = True
            # update_todos.append(todo)
        Todo.objects.bulk_update(todos,['checked'])
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    # update_todos = []
    # todos = Todo.objects.filter(checked=False).update(checked=True)
    # # for todo in todos:
    # #     todo.checked = True
    # update_todos.append(todos)
    
    # Todo.objects.bulk_update(update_todos,['checked'])
       



# TodoCheckedAll
# serializer_class = TodoSerializer

    #     # new
#     # queryset = Todo.objects.filter(checked=False)
#     # serializer_class = TodoSerializer()
    
#     # # todos = Todo.objects.filter(checked=False)
#     # # for todo in todos:
#     # #     todo.checked = True
#     # #     todo.save()






# class TodoDeleteandUpdate(generics.UpdateAPIView):
#     queryset = Todo.objects.filter(checked=True)
#     serializer_class = TodoSerializer  
       
#     def get_queryset(self):
#         # res = super().get_queryset()
#         filter = self.request.query_params.get('filter')
#         if filter == 'complited':
#             return self.request.filter(checked=True).delete()

        # ids = request.query_params.get('ids').split(',')
        # queryset = Todo.objects.filter(id__in=ids)
        # serializer = TodoSerializer(queryset, many=True)
        # return Response(serializer.data)
    # def delete(self, request, *args, **kwargs):
    #     ids = request.query_params['ids']
    #     delete_todos = self.queryset.filter(id__in=ids)
    #     serializer_class = TodoSerializer(ids, many=True)

    #     delete_todos.delete()
    #     return Response( self.serializer_class(delete_todos,many=True).data) 

    
    
    # filterset_class = TodoFilter


# class TodoCheckedDelete(generics.DestroyAPIView, generics.ListCreateAPIView,):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def delete_queryset(self):
#         # res = super().get_queryset()
#         ids = self.request.query_params.get('ids')
        
#         todos = Todo.objects.filter(id__in=ids)
#         for todo in todos:
#             todo.delete()
#         serializer = TodoSerializer(ids, many=True)
#         return serializer.data    

   
# class TodoCheckedDelete(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     @action(methods=["DELETE"], details=False, )
#     def delete(self, request: Request):
#         delete_id =request.data
#         delete_todos = self.queryset.filter(id__in=delete_id)
        
#         delete_todos.delete()
#         return Response( self.serializer_class(delete_todos,many=True).data) 


   
# class TodoCheckedDelete(APIView):
#     def delete(self, request, *args, **kwargs):
#         ids = request.query_params.get('ids').split(',')
#         queryset = Todo.objects.filter(id__in=ids)
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def delete(self, request, *args, **kwargs):
#         ids = request.query_params('ids')
#         if ids:
#             queryset = Todo.objects.filter(id__in=ids)
#             queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ids = request.query_params[“ids”]
# serializer =Serializer(ids, many=True)
# serializer.is_valid(raise_exception=True)
# todo = serializer.validation_data


# class TodoCheckedDelete(APIView):
#     queryset = Todo.objects.all()
    
#     def delete_queryset(request):
#         ids = request.query_params["ids"]
#         albums = Album.objects.filter(id__in=ids)
#         for album in albums:
#             album.delete()
#         serializer = AlbumSerializer(albums, many=True)
#         return Response(serializer.data)
#     def delete(self, request, *args, **kwargs):
#         ids = request.query_params('ids')
#         if ids:
#             queryset = Todo.objects.filter(id__in=ids)
#             queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# ids = request.query_params[“ids”]
# serializer =Serializer(ids, many=True)
# serializer.is_valid(raise_exception=True)
# todo = serializer.validation_data

# !!!!!!!!!!!
# class DeleteCheckedTodo(APIView):
#     def get(self, request, pk_ids):
#         ids = [int(pk) for pk in pk_ids.split(',')]
#         contactObject = Todo.objects.filter(id__in=ids)
#         serializeContactObject = TodoSerializer(contactObject, many=True)
#         return Response(serializeContactObject.data)

#     def delete(self, request, pk_ids):
    
#         ids = request.query_params('ids')
#         res = Todo.objects.filter(id__in=ids)
#         serializer = TodoSerializer(res, many=True)
        
#         return Response(serializer.data)

#  !!!!!!!!!!!
 
 
    # def delete(self, request, *args, **kwargs):
#         ids = request.query_params.get('ids').split(',')
#         queryset = Todo.objects.filter(id__in=ids)
#         serializer = TodoSerializer(queryset, many=True)
#         return Response(serializer.data)


# class TodoCheckedDelete(generics.DestroyAPIView):
#     queryset = Todo.objects.filter(checked=True)
#     serializer_class = TodoSerializer(many=True)
    
#     def delete(self, request, *args, **kwargs):
#         todo = Todo.objects.filter(checked=kwargs[True])
#         if todo.count() > 0:
#            todo.delete()
#            return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(status=status.HTTP_404_OK)
        

    

# class TodoCheckedDelete(viewsets.ModelViewSet):
#     queryset = Todo.objects.all
#     serializer_class = TodoSerializer
    
#     def get_queryset(self):
#         return self.queryset.filter(is_deleted=False)
        
#     def batch_destroy(self, request):
#         ids = request.data.get('ids', [])
#         self.queryset.filter(id__in=ids).delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class TodoCheckedDelete(mixins.DestroyModelMixin,
#                     generics.ListCreateAPIView):
#     model = Todo
#     # queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

#     def get_queryset(self):
#         filter = self.request.query_params.get('filter')
#         if filter == 'complited':
#             return Todo.filter(checked=True)
#         return Todo.objects.filter(checked=True)

    # def pre_save(self, obj):
    #     obj.user = self.request.user
    #     obj.notepad = get_object_or_404(Notepad, user=self.request.user, pk=self.kwargs['notepad_pk'])

    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)
        
        
# def get_queryset(self):
#         res = super().get_queryset()
#         filter = self.request.query_params.get('filter')
#         if filter == 'complited':
#             return res.filter(checked=True)
#         elif filter == 'active':
#             return res.filter(checked=False)
#         else:
#             return res


# class BulkDeleteView(View):
#     model = None

#     def post(self, request, *args, **kwargs):
#         delete_ids = request.POST['delete_ids'].split(',')  # should validate
#         self.model.objects.filter(pk__in=delete_ids).delete()
#         return render / redirect