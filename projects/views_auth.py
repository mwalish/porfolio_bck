from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    """Authenticate user and return token."""
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': user.username})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def check_auth(request):
    """Check if current user is authenticated."""
    if request.user.is_authenticated:
        return Response({'authenticated': True, 'user': request.user.username})
    return Response({'authenticated': False}, status=status.HTTP_401_UNAUTHORIZED)

