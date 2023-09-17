from django.contrib import admin
from django.urls import path,include
from bookstore import views

urlpatterns = [
    path('', views.all_tasks_view),
    path('admin/', admin.site.urls),
    path('api/', include('bookstore.urls', namespace='bookstore'))
]
