from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField()
    photo = models.ImageField(upload_to="blogs/", blank=True, null=True)
    blog_text = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blogs, self).save(*args, **kwargs)
