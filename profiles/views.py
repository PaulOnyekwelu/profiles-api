from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from profiles import serializers, models, permissions


class UserProfileViewSet(ModelViewSet):
    '''APi endpoints for the userprofile'''
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('email', 'first_name', 'last_name')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated)


class UserLoginAPIView(ObtainAuthToken):
    '''Handles user login token generation'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class FeedViewSet(ModelViewSet):
    '''api endpoints for feeds'''
    serializer_class = serializers.FeedSerializer
    queryset = models.FeedModel.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnFeeds, IsAuthenticated)

    def perform_create(self, serializer):
        '''save logged user as user_profile'''
        serializer.save(user_profile=self.request.user)


# class UserProfileView(ViewSet):
#     '''API endpoints for the userprofile'''
#     # list, create, retrieve, update, partial_update, destroy
#     serializer_class = serializers.UserProfileSerializer
#     model = models.UserProfile

#     def list(self, request):
#         serializer = self.serializer_class(
#                   self.model.objects.all(), many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         try:
#             user = self.model.objects.get(pk=pk)
#             serializer = self.serializer_class(user)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response({}, status=status.HTTP_404_NOT_FOUND)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.create(serializer.validated_data)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
