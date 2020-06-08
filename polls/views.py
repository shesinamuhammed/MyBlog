from django.shortcuts import render
from .forms import PostForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse,reverse_lazy
from polls.models import Blog
from django.views.generic.edit import DeleteView 
from django.views.generic.detail import DetailView 

class BlogCreateView(CreateView):

	template_name = 'blogs.html'
	form_class = PostForm		
	success_url = reverse_lazy('bloglist')

class BlogListView(ListView):
	model = Blog
	template_name = 'bloglist.html'

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title','body']
    template_name = 'blogs.html'
    success_url = reverse_lazy('bloglist')

class BlogDeleteView(DeleteView): 
    
    model = Blog 
    template_name = 'blogdelete.html'
    success_url =reverse_lazy('bloglist')

class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blogdetail.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

		
        
        
        
