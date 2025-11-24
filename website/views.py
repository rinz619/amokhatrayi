from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from website.helper import renderhelper, is_ajax
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
# from website.custom_permision import LoginRequiredMixin, AdminLoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from superadmin.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.db.models import Q


class index(View):
    def get(self, request):
        context = {}
        context['category'] = Category.objects.all()
        context['course'] = Courses.objects.all()
        return renderhelper(request, 'home', 'index',context)


class CoursesView(View):
    def get(self, request,slug):
        context = {}
        if slug:
            context['course'] = Courses.objects.filter(category__slug=slug)
        else:
            context['course'] = Courses.objects.all()
        return renderhelper(request, 'course', 'courses',context)


class CourseDetailView(View):
    def get(self, request,slug):
        context = {}

        context['course'] = Courses.objects.get(slug=slug)
        return renderhelper(request, 'course', 'course-single',context)


