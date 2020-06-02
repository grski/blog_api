from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from api.users.serializers import UserSerializer
from django.contrib.auth.models import User


from rest_framework.authtoken.models import Token

class UserCreate(APIView):
    """
    Creates the user.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

