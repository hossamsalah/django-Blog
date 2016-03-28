from django.db import models
from django.contrib.auth.models import User


class UserProfile (models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    about = models.TextField(blank=True)
    image = models.FileField(upload_to='photos/%Y/%m/%d', blank=True)


    def __unicode__(self):
        return self.user.username



class Category (models.Model):
    # Art = 'Art'
    # Fun = 'Fun'
    # Educational = 'Educational'
    # Sports = 'Sports'
    # category_choices = ((Art, 'Art'), (Sports, 'Sports'), (Educational, 'Educational'), (Fun, 'Fun'))
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category


class Blog (models.Model):
    title = models.CharField(max_length=150, default="no title")
    body = models.TextField(default="None")
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=1)
    category = models.ForeignKey(Category, default="none")

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField(default="")
    blog = models.ForeignKey(Blog)
    author = models.ForeignKey(User, default=1)

    def __str__(self):
        return self.comment
