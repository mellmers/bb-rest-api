from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import *


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request: Request, *args, **kwargs):
        """
        If provided 'pk' is "me" then return the current user.
        """
        if kwargs.get('pk') == 'me':
            return Response(self.get_serializer(request.user).data)
        return super().retrieve(request, args, kwargs)

    # @action(methods=["get"], detail=False, url_path="recent", url_name="recent")
    # def get_recent_movies(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     queryset = queryset.filter(status=1).order_by("-timestamp")[:12]
    #     serializer = MovieListSerializer(queryset, many=True)
    #     """
    #     if some condtion:
    #         call check_data_tables() method
    #     """
    #     if condition:
    #         result = result = self.check_data_tables(queryset)
    #         return processed
    #         response
    #     return Response(serializer.data)
