from django.db import models

class Post(models.Model):
    class Meta:
      db_table = 'blog_post' 

    title = models.CharField(max_length=255)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
    'records.CustomUser',
    on_delete=models.SET_NULL, 
    null=True,
    blank=True
    )
    image = models.ImageField(upload_to='images/', default='CeO.JPG')
    slug = models.SlugField(unique=True)
