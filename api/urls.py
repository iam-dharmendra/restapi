from django.urls import  path
from . import views

urlpatterns=[
    path('alldata/',views.studentview.as_view()),
    path('data/<int:id>',views.studentview.as_view()),
]
