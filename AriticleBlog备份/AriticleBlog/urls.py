"""AriticleBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf.urls.static import static
from . import settings
from Article.views import login,index,logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path("article/",include("Article.urls")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("login/",login),
    path("logout/",logout),
    re_path("^$",index),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)