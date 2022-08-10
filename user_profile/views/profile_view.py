from rest_framework import generics
from ..models import Profile
from ..serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        record = Profile.objects.filter(user=user)
        if record is None or record == "":
            return "No Data Found"
        return record

    def perform_create(self, serializer):
        serializer.save()

profile_list_view = ProfileListView.as_view()


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

profile_update_view = ProfileUpdateView.as_view()