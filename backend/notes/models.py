from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

User = get_user_model()


class Note(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique_for_date="created_at")
    content = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["created_at"])]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Note title: {self.title} by {self.owner}"

    def get_absolute_url(self):
        return reverse(
            "note:note_detail",
            args=[
                self.created_at.year,
                self.created_at.month,
                self.created_at.day,
                self.slug,
            ],
        )
