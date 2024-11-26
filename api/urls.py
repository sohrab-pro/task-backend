from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Login,
    Signup,
    TaskViewSet
)

router = DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view()),
    path('signup/', Signup.as_view()),
]
