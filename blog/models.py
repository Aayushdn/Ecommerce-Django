from django.db import models

# Create your models here.
class Blogpost(models.Model):

    Choices = (
        ('Design','Design'),
        ('interface','interface'),
        ('shop','shop'),
        ('suggestion','suggestion')
    )

    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    heading0 = models.CharField(max_length=500, default = "")
    cheading0 = models.CharField( max_length=50000 , default = "")
    heading1 = models.CharField(max_length=500, default = "")
    cheading1 = models.CharField(max_length=50000 , default = "")
    heading2 = models.CharField(max_length=500, default = "")
    cheading2 = models.CharField( max_length=50000, default = "")
    category = models.CharField(max_length=50 , choices = Choices,default = '')
    image = models.ImageField(upload_to = "blog/images",default='')
    blog_pub_date = models.DateField()

    def __str__(self):
        return self.title
