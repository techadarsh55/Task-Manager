
from django.contrib import admin
from django.urls import path,include
from home import urls

admin.site.site_title = "Task Planer"
admin.site.site_header = 'Task Manager'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),

]
