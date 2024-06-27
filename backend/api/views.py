from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import TaskSerializer
from .models import Task


class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskDetailView(APIView):
    def delete(self, request, pk):
        Task.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
