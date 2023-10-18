import uuid
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=127)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=127)
    created_date = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)



    def __str__(self):
        return self.title