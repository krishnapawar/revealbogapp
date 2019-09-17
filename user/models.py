from django.db import models
from django.utils import timezone
from PIL import Image

# Create your models here.
class photfolio(models.Model):
	popupimg = models.ImageField(upload_to='media')
	item = models.CharField( max_length=150)
	date = models.DateTimeField()

	def save(self):
		super().save()
		img = Image.open(self.popupimg.path)

		if img.height > 400 or img.width > 500 :
			output_size = (400,500)
			img.thumbnail(output_size)
			img.save(self.popupimg.path)