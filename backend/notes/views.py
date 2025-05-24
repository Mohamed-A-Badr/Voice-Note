from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.select_related("owner").filter(owner=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)

        return Response(
            {"message": "note added successfully"},
            status=status.HTTP_201_CREATED,
        )


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.select_related("owner").filter(owner=user)

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get("slug")
        year = int(self.kwargs.get("year"))
        month = int(self.kwargs.get("month"))
        day = int(self.kwargs.get("day"))
        return queryset.get(
            slug=slug,
            created_at__year=year,
            created_at__month=month,
            created_at__day=day,
        )


note_list_create = NoteListCreateView.as_view()
note_detail = NoteDetailView.as_view()
