"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from account import views as account_views
from quiz import views as quiz_views
from entry import views as entry_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', account_views.login, name="login"),
    url(r'^feed/', account_views.feed_seolgi, name="feed"),
    url(r'^quizzes/', quiz_views.get_quizzes, name="get_quizzes"),
    url(r'^index/', entry_views.get_index, name="get_index"),
]

quiz_views.update_quizzes() # When the project starts, execute "update_quizzes".
