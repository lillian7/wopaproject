from django import forms
# Create your models here.
from blog.models import Blog, Category

class PostForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields =('title','slug','category','body', )

class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields =('title','slug',)