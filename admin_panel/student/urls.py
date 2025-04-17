from django.urls import path 
from student.views import registration,login
urlpatterns = [
  path('reg/', registration, name='registration'),
  path('log/', login, name='login'),
]
