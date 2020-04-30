"""project URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from owner import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='owner'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('products/',views.products,name='products'),
    path('signup/',views.signupuser,name='signupuser'),
    path('logout/',views.logoutuser,name='logoutuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post_detail/<int:val>/',views.post_detail,name='post_detail'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)