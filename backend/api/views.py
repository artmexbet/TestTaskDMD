from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import TaskSerializer
from .models import Task
from .utills import format_list


class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        # Форматируем данные для дерева на фронтенде
        data = format_list(serializer.data)
        return Response(data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskDetailView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            Task.objects.get(pk=pk).delete()
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if 'status' in request.data and request.data['status'] != task.status:
            if request.data['status'] == 'completed':
                try:
                    task.complete()
                except ValueError:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            elif request.data['status'] == 'paused':
                task.pause()

        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
