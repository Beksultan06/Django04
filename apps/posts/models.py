from django.db import models

CATEGORY_CHOICES = (
    ("SP", "Спорт"),
    ("POL", "Политика"),
    ("ECO", "Экономика"),
    ("SOC", "Общество"),
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, default="SOC")
    status = models.BooleanField(default=True)
    cover = models.ImageField(default="image.jpg", upload_to="uploads/posts", blank=True)

    def __str__(self):
        return f"{self.title} - {self.created}"
