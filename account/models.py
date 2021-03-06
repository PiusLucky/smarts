from django.db import models


class Note(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = "-created",

	def __str__(self):
		return self.title


