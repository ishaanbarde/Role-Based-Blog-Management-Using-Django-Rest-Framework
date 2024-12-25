# DJANGO
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

# REST FRAMEWORK
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# PROJECT
from .models import CustomUser
from .serializers import custUser_Serialization
from .permissions import IsOwner


def getToken(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        if CustomUser.objects.count() == 0:
            request.data['role'] = 'Owner'

        if CustomUser.objects.filter(username = request.data.get('username')).exists():
            return Response(
                {"message":"User with this username already exists"}, 
                status=400)
           
        serializer = custUser_Serialization(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User created successfully"},
                status=201,)
        
        return Response(
            {"message":"Bad Request",
            "errors":serializer.errors},
            status = 400)
    except:
        return Response(
            {"message":"Something went wrong"},
            status = 500)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=400
            )

        user = authenticate(username=username, password=password)

        if user is not None:
            tokens = getToken(user)

            return Response({
                "message": "Login successful!",
                "tokens": tokens,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            }, status=200)
        else:
            return Response(
                {"error": "Invalid credentials. Please try again."},
                status=401
            )
    except:
        return Response(
            {"error": "Something went wrong!"},
            status=500)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsOwner])
def createUser(request):
    try:
        role = request.data.get('role')

        if role not in ['Admin','Member']:
            return Response(
                {"message":"Only the owner is allowed"},
                status = 400)
        
        serializer = custUser_Serialization(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!", "user": serializer.data}, status=201)
        return Response(serializer.errors, status=400)
    except:
        return Response(
            {"error": "Something went wrong!"},
            status=500)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_users(request):
    try:
        users = CustomUser.objects.all()
        serializer = custUser_Serialization(users, many=True)

        return Response(serializer.data, status=200)
    except:
        return Response(
            {"error": "Something went wrong!"},
            status=500)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsOwner])
def update_role(request, user_id):

    user = get_object_or_404(CustomUser, id=user_id)
    role = request.data.get('role')

    if role not in ['Admin', 'Member']:
        return Response({"message": "Role must be either 'Admin' or 'Member'."}, status=400)

    user.role = role
    user.save()
    return Response({"message": "User role updated successfully!"}, status=200)
