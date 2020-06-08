from django import forms

from .models import Blog

class PostForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title', 'body')
    def clean(self):
    	cleaned_data = super().clean()
    	title = cleaned_data.get('title')
    	if len(title)<5:
    		self.add_error('title','Please enter longer number')
    	return cleaned_data
