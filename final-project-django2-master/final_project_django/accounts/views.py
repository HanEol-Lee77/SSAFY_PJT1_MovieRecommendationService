from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .models import User
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def admin_accounts(request):
    accounts = User.objects.all()
    serializers = UserSerializer(accounts, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def detail(request, user_pk):
    account = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(account)
    return Response(serializer.data)

# @api_view(['POST'])
# def signup(request):
#     serializer = UserSerializer(request.user)
#     if user.is_valid():
#         user.save()
#         return Response({message: "회원가입이 완료되었습니다."})
#     return Response(status=400)

# @api_view(['GET'])
# def signout(request):
#     request.user.delete()
#     return Response({message: "회원탈퇴가 완료되었습니다."})

# @api_view(['GET', 'POST'])
# def login(request):
#     if request.user.is_authenticated:
#         return Response({message: "이미 로그인 되어있습니다."})
    
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.POST)
#         if serializer.is_valid():
#             auth_login(request, serializer.get_user())
#     else:
#         serializer = UserSerializer()
#     return Response(serializer.data)

# def logout(request):
#     pass

@api_view(['POST'])
def create(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(status=200)

@api_view(['POST'])
def delete(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    return Response(status=200)

@api_view(['POST'])
def update(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(data=request.data, instance=user)
    if serializer.is_valid():
        serializer.save()
    return Response(status=200)

class UserAPIView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)