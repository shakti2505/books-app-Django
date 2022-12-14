"""bookdatabase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users import views as users_view
# importing for login fucntionility 
from django.contrib.auth import views as authentications_views

# Imports for uploading profile picture to the profile 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    #/register/
    path('register/',users_view.register, name='register'),
    #/Login/ using inbuilt login views
    path('login/', authentications_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    #/Logout/ using inbuilt logout view
    path('logout/', authentications_views.LogoutView.as_view(template_name ='users/logout.html'), name='logout'),
    #/profile/
    path('profile/', users_view.profile_page, name='profile')

]



urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)