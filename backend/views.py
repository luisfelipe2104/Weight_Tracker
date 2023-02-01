from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Weight
from .serializers import WeightSerializer

# Create your views here.
class AllWeightView(generics.ListAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeightSerializer

class createWeight(APIView):
    def post(self, request, format=None):
        serializer = WeightSerializer(data=request.data)
        if serializer.is_valid():
            weightData = serializer.data.get('weight')
            date = serializer.data.get('date')
            weight = Weight(weight=weightData, date=date)
            weight.save()
            return Response({'success': "Data saved!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'failed': 'Failed in saving data'}, status=status.HTTP_400_BAD_REQUEST)

class updateWeight(APIView):
    def post(self, request, pk):
        serializer = WeightSerializer(data=request.data)
        if serializer.is_valid():
            weight = Weight.objects.get(id=pk)
            weightData = serializer.data.get('weight')
            weight.weight = weightData
            weight.save()
            return Response({'success': "Data saved!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'failed': 'Failed in saving data'}, status=status.HTTP_400_BAD_REQUEST)

class deleteWeight(APIView):
    def delete(self, request, pk):
        weight = Weight.objects.get(id=pk)
        weight.delete()
        return Response({'success': "Task deleted!"}, status=status.HTTP_200_OK)