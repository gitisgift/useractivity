from django.db import models
from django.contrib.auth.models import User
import json
from django.utils import timezone

class UserInfo(models.Model):

	id=models.CharField(max_length=125,primary_key=True,blank=False)
	real_name=models.CharField(max_length=225,blank=False,null=False)
	tz=models.CharField(max_length=225,blank=False,null=False)

	def __str__(self):
		return self.real_name
	

class UserTime(models.Model):

	user=models.ForeignKey(UserInfo,related_name='activity_periods',on_delete=models.PROTECT)
	start_time=models.DateTimeField(auto_now=True,blank=False)
	end_time=models.DateTimeField(auto_now=True,blank=False)

	def __str__(self):
		return str({"start_time":(self.start_time).strftime("%b %d %y %I:%M%p"),
			"end_time":(self.end_time).strftime("%b %d %Y %I:%M%p")})
		
