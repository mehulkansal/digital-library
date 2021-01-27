"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from Pages.views import home_view,about_view,contact_view,signin_view,signup_view,welcome_view,select_view,bookreturn
from Book.views import handle_signin,handle_signup,handle_logout
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    path('about/', about_view),
    path('contactus/', contact_view),
    path('signin/', signin_view),
    path('signin/succes/', handle_signin,name='signin'),
    path('signup/', signup_view),
    path('signup/su/', handle_signup),
    path('signin/welcome/', welcome_view,name='welcome'),
    path('signin/admin/', admin.site.urls),
    path('signin/welcome/select/',select_view ),
    path('signup/welcome/', welcome_view),
    path('signin/welcome/logout/', handle_logout),
    path('logout/', handle_logout),
    path('signin/welcome/return/',bookreturn ),

]
