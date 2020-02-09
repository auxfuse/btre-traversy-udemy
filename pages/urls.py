'''
Imports the path() function. This import is necessary for the URL dispatcher
to work and is common to all urls.py files.
'''
from django.urls import path

'''
Imports the local views.py file. The dot operator (“.”) in this case is 
shorthand for the current package, so this is saying “import all views from 
the current package (pages)”.
'''
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]