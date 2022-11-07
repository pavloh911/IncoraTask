from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer
from IncoraTask.wsgi import server

CustomUserModel = get_user_model()


class UserListCreateView(ListCreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(),]
        else:
            return [AllowAny(),]


class UserRetrieveView(RetrieveAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        user = self.get_serializer(obj, data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        server.emit('update', user.data)

        return Response(data=user.data, status=status.HTTP_200_OK)
