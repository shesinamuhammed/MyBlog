from .forms import PostForm, SignUpForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse,reverse_lazy
from polls.models import Blog
from django.views.generic.edit import DeleteView 
from django.views.generic.detail import DetailView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse, Http404
  


class LoginView(auth_views.LoginView):
   template_name = 'login.html'
   success_url = reverse_lazy('bloglist')

class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
        



class BlogCreateView(LoginRequiredMixin,CreateView):
    
    template_name = 'blogs.html'
    form_class = PostForm       
    success_url = reverse_lazy('bloglist')

    def form_valid(self,form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)






class BlogListView(ListView):
    model = Blog
    template_name = 'bloglist.html'

class BlogUpdateView(LoginRequiredMixin,UpdateView):
   
    model = Blog
    fields = ['title','body']
    template_name = 'blogs.html'
    success_url = reverse_lazy('bloglist')
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise Http404("You are not allowed to edit this Post")
        return super(BlogUpdateView, self).dispatch(request, *args, **kwargs)

class BlogDeleteView(DeleteView): 
    
    model = Blog 
    template_name = 'blogdelete.html'
    success_url =reverse_lazy('bloglist')

class BlogDetailView(DetailView):

    model = Blog
    template_name = 'blogdetail.html'


        
        
        
        
