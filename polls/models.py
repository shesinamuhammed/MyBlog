from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

