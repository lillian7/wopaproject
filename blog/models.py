from django.db import models
from django.db.models import permalink

# Create your models here.

#first a database table called blog
class Blog(models.Model):
    #the fields to be created in the table blogs
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    body = models.TextField()
    posted = models.DateTimeField(db_index =True, auto_now_add =True)
    category = models.ForeignKey('blog.Category')

    #unicode will set the text reference 'title' for each record
    def __unicode__(self):
        return '%s' % self.title

    @permalink
    #decorator to hold the right url format
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})


#another database table called ctegory
class Category(models.Model):
    title = models.CharField(max_length = 100, db_index = True)
    slug = models.SlugField(max_length = 100, db_index = True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})
