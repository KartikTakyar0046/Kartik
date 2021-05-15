from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    def __str__(self):
        return self.name
    

class Gift(models.Model):
    book=models.ForeignKey(Book,related_name="book",on_delete=models.CASCADE)
    sender=models.CharField(max_length=100)
    def __str__(self):
        return self.sender

        