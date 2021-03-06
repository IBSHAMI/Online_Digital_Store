from django.db import models

# create products model for database
digital_products_categories = (
    ('1', 'Books'),
    ('2', 'Movies'),
    ('3', 'Music'),
    ('4', 'Games'),
    ('5', 'Software'),
    ('9', 'Other'),
)


class Products(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=1, choices=digital_products_categories)
    product_slug = models.SlugField()
    price = models.PositiveIntegerField()
    desc = models.TextField(max_length=1000, blank=True, null=True)
    product_pic = models.ImageField(upload_to='products/pictures', default='products/no-img.jpg', blank=True, null=True)
    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(upload_to='products/files', blank=True, null=True)

    # auto generate publish date
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
