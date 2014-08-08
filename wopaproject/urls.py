from django.conf.urls import patterns, include, url

from django.contrib import admin
from blog import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wopaproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

   (r'^$', 'blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'blog.views.view_post', 
    name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'blog.views.view_category', 
    name='view_blog_category'),
url(r'^post/new/$', views.post_new, name ='post_edit'),
url(r'^category/new/$', views.category_new, name ='category_edit'),
)
