from django.db import models

# Create your models here.
class Record(models.Model):
	creat_at = models.DateTimeField(auto_now_add = True)
	first_name = models.CharField(max_length = 15)
	last_name = models.CharField(max_length = 10)
	email = models.EmailField()
	phone = models.CharField(max_length=10)

	def __str__(self):
		return(f"{self.first_name}{self.last_name}")
