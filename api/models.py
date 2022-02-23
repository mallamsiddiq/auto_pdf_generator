from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []




class Transaction(models.Model):
	description =models.TextField(blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	class Meta:
		ordering = ['-id']
	def __str__(self):
		return (f"{self.discripton}") if self.discripton else 'this text has no desc'
	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})


class Document(models.Model):
	title =models.CharField(max_length=1000, blank=True,null=True)
	doc = models.FileField(upload_to='transsaction_files')
	transaction = models.ForeignKey(Transaction,related_name='documents', on_delete=models.CASCADE)
	#from_api =models.BooleanField(default=True,blank=True,null=True) 


	class Meta:
		ordering = ['-id']
	def __str__(self):
		return (f"{self.title}")
	def get_absolute_url(self):
		return reverse('item-detail', kwargs={'pk': self.pk})



