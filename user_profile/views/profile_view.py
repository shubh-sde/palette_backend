from rest_framework import generics
from ..models import Profile
from ..serializers import ProfileSerializer


class ProfileListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # title = serializer.validated_data.get('title')
        # content = serializer.validated_data.get('content')
        # if content is None:
        #     content = title
        serializer.save()#content=content)

profile_list_view = ProfileListView.as_view()


# class RecordDetailedView(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
    
# products_record_view = RecordDetailedView.as_view()


# # class RecordCreate(APIView):
# #     def post(self,request):
# #         serializer = ProductSerializer(data = request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             print(serializer.data)
# #             data = serializer.data
# #             return Response(data)


# # class RecordView(APIView):

# #     def get_record_by_pk(self,pk):
# #         try:
# #             return Products.objects.get(pk=pk)
# #         except:
# #             return Response({"Error :":"Couldn't ffin any records!"},status=status.HTTP_404_NOT_FOUND)

# #     def get(self,request,pk):
# #         record = self.get_record_by_pk(pk)
# #         serializer = ProductSerializer(record)
# #         return Response(serializer.data);