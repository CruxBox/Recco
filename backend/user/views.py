
from django.contrib.auth import authenticate,get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import UserSerializer, RegisterSerializer,UsersSerializer
from rest_framework import status
from rest_framework.response import Response
User=get_user_model()

@permission_classes((AllowAny,))
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        print("kkk")
        serializer = self.get_serializer(data=request.data)
        print(serializer.is_valid())
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": Token.objects.get_or_create(user=user)[0].key,
        }, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    description: API for login.
    parameters:
      - name: username
        type: string
        required: true
        location: form
      - name: password
        type: password
        required: true
        location: form
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
    "user": UserSerializer(user).data,
    "token": Token.objects.get_or_create(user=user)[0].key,
    }, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(('DELETE',))
@authentication_classes((TokenAuthentication, ))
def logout(request):
    Token.objects.get(user=request.user).delete()
    return Response({'message':'Logout Successful'},status=status.HTTP_200_OK)

@csrf_exempt
@api_view(('GET',))
@authentication_classes((TokenAuthentication, ))
def list_users(request):
    users = User.objects.all().exclude(username=request.user.username)
    return Response(UsersSerializer(users,many=True).data,status=status.HTTP_200_OK)
