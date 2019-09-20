from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.
class clients(models.Model):
	name = models.CharField(max_length = 20)
	email = models.CharField(max_length = 60)
	subject = models.CharField(max_length = 250)
	massage = models.CharField(max_length = 1050)
	date = models.DateTimeField()

	

class banner(models.Model):
	banner1 = models.ImageField(upload_to='bennne')
	banner2 = models.ImageField(upload_to='bennne')
	banner3 = models.ImageField(upload_to='bennne')
	banner4 = models.ImageField(upload_to='bennne')
	banner5 = models.ImageField(upload_to='bennne')

	def get_absolute_url(self):
		return reverse('home')


	def save(self):
		super().save()

		img2 = Image.open(self.banner1.path)
		if img2.height > 900 or img2.width > 1920: 
			output_size = (900,1920)
			img2.thumbnail(output_size)
			img2.save(self.banner1.path)

	def save(self):
		super().save()

		img3 = Image.open(self.banner3.path)
		if img3.height > 900 or img3.width > 1920: 
			output_size = (900,1920)
			img3.thumbnail(output_size)
			img3.save(self.banner3.path)

	def save(self):
		super().save()

		img1 = Image.open(self.banner4.path)
		if img1.height > 900 or img1.width > 1920: 
			output_size = (900,1920)
			img1.thumbnail(output_size)
			img1.save(self.banner4.path)

	def save(self):
		super().save()

		img4 = Image.open(self.banner5.path)
		if img4.height > 900 or img4.width > 1920: 
			output_size = (900,1920)
			img4.thumbnail(output_size)
			img4.save(self.banner5.path)

	def save(self):
		super().save()

		img5 = Image.open(self.banner2.path)
		if img5.height > 900 or img5.width > 1920: 
			output_size = (900,1920)
			img5.thumbnail(output_size)
			img5.save(self.banner2.path)		

