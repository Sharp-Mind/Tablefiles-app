from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator





class TableFile(models.Model):   

    name = models.CharField(max_length= 255, blank=False, null=False, verbose_name='Description')
    file = models.FileField(upload_to= 'files/', null=True, validators=[FileExtensionValidator(['csv'])], verbose_name='File (.csv only)')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __repr__(self):
        self.slug = self.name
        return f'TableFile({self.name}, {self.file}, {self.slug})'

    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):      
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    