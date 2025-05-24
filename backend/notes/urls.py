from django.urls import path

from . import views

app_name = "note"

urlpatterns = [
    path("", views.note_list_create, name="note_list_create"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.note_detail,
        name="note_detail",
    ),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/audio/",
        views.text_to_speech,
        name="voice_note",
    ),
]
