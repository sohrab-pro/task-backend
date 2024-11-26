from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from.serializers import *

# Create your views here.
class Login(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'message': 'Logged in Successfully!', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class Signup(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        if Account.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists!'}, status=status.HTTP_400_BAD_REQUEST)

        if Account.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists!'}, status=status.HTTP_400_BAD_REQUEST)

        if len(password) < 8:
            return Response({'error': 'Password should be at least 8 characters long!'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'User created successfully!', 'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()
        return Response({'status': 'success', 'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)