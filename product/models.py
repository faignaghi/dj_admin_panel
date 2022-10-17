from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

####### Product Model ################

class Product(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    description = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return self.name
    def how_many_reviews(self):
        count = self.reviews.count()
        return count
    
    
############ Review Model ##############
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}" 
    