"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('blogcreate/', views.BlogCreateView.as_view(),name='blogcreate'),
    path('',views.BlogListView.as_view(),name='bloglist'),
    path('blog/edit/<int:pk>/',views.BlogUpdateView.as_view(),name='blogedit'),
    path('blog/delete/<int:pk>/',views.BlogDeleteView.as_view(),name='blogdelete'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(),name='blogdetail'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('logout/',LogoutView.as_view(),name='logout')
    
]


