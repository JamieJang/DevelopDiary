from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=1024,unique=True)
    
    def __str__(self):
        return self.name

class Note(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

class Diary(models.Model):
    title = models.CharField(max_length=1024)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']
