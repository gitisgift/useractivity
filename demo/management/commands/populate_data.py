from django.core.management.base import BaseCommand
from datetime import datetime
import json
from django.conf import settings
from demo.models import UserInfo,UserTime
import os



class Command(BaseCommand):
	help = 'insert values into table'

	def add_arguments(self, parser):

		parser.add_argument('json', type=str)
		#parser.add_argument('-j','--json', action='store_true', help='Create an admin account')
		#pass
	def handle(self, *args,**kwargs):
		if kwargs['json']:
			filename=kwargs['json']
			#self.stdout.write(os.path.join(settings.BASE_DIR,'jsondata')+os.path.sep+filename)
			file_path=str(os.path.join(settings.BASE_DIR,'jsondata')+os.path.sep+filename)
			#self.stdout.write(file_path)
			try:
				f=open(file_path,)
				data = json.load(f)
				if data['ok']:
					#self.stdout.write(str(data['members'][0]['id']))
					for i in range(len(data['members'])):
						id=data['members'][i]['id']
						real_name=data['members'][i]['real_name']
						tz=data['members'][i]['tz']
						for_other_table=data['members'][i]['activity_periods']

						#userinfo=UserInfo.objects.create(id=id,real_name=real_name,tz=tz)
						userinfo=UserInfo(id=id,real_name=real_name,tz=tz)
						userinfo.save()
						for j in range(len(for_other_table)):
							start_time=for_other_table[j]['start_time']
							end_time=for_other_table[j]['end_time']
							start_time_obj=datetime.strptime(start_time,"%b %d %Y %I:%M%p")
							end_time_obj=datetime.strptime(end_time,"%b %d %Y %I:%M%p")

							ut=UserTime(user=userinfo,start_time=start_time_obj,end_time=end_time_obj)
							ut.save()

						


					self.stdout.write("Succesfully inserted")
				
					#self.stdout.write(data['members'][0])
			except Exception as e:

				return str(e)
				#self.stdout.write(e)

			#return "hi"
			#self.stdout.write(kwargs['json'])
        