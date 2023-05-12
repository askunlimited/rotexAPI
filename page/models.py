from django.db import models
from django.utils.text import slugify

# Create your models here.


def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Page(models.Model):
    title = models.CharField(max_length=225, blank=False)
    slug = models.SlugField(null=False, unique=True)
    body = models.TextField()
    featured_image = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)


