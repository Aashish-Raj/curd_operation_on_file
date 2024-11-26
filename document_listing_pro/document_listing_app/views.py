from rest_framework.views import APIView
from  rest_framework.response import Response
from rest_framework import status


# Create your views here.

class DocumentListingView(APIView):
    def get(self,request):
        return Response({"message":"Successs"},status=status.HTTP_200_OK)
