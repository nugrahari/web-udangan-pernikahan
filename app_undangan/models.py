from django.db import models
# from django.template.defaultfilters import slugify # new
# from django.urls import reverse
from embed_video.fields import EmbedVideoField
class Pengantin(models.Model):
	nama = models.CharField(max_length=200, null=True, blank=True)
	keterangan = models.CharField(max_length=200, null=True, blank=True)
	gambar = models.ImageField(upload_to ='galery/')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nama

class LiveVideo(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	
	video = EmbedVideoField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('article_detail', kwargs={'slug': self.slug})

	# def save(self, *args, **kwargs): # new
	# 	if not self.slug:
	# 		self.slug = slugify(self.title)
	# 	return super().save(*args, **kwargs)

class Galery(models.Model):
	title = models.CharField(max_length=200, null=True, blank=True)
	gambar = models.ImageField(upload_to ='galery/')
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

class TamuUndangan(models.Model):
	nama = models.CharField(max_length=200, null=True, blank=True)
	keterangan = models.CharField(max_length=200, null=True, blank=True)
	
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nama

class Pesan(models.Model):
	nama = models.OneToOneField(TamuUndangan, on_delete=models.CASCADE)
	ucapan = models.TextField()
	sumbangan = models.CharField(max_length=200, null=True, blank=True)
	tampilkan = models.BooleanField(default=False)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.ucapan


