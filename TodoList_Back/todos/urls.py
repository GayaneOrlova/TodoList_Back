# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from todos import views

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'todos', views.TodoViewSet)

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

urlpatterns = [
    path('todos/', views.TodoList.as_view()),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view()),
    path('todos/<int:pk>/', views.TodoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)