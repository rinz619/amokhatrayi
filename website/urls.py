from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website import views


app_name = 'website'

urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('courses',views.CoursesView.as_view(),name='courses'),
    path('courses/<str:slug>',views.CoursesView.as_view(),name='courses'),
    path('course-details/<str:slug>',views.CourseDetailView.as_view(),name='course-details')
]