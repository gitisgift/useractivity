
from rest_framework import serializers
from .models import UserInfo,UserTime

class UserSerializer(serializers.ModelSerializer):

	activity_periods= serializers.StringRelatedField(many=True)
	class Meta:
		model=UserInfo
		fields =['id','real_name','tz','activity_periods']

		
