from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.
class BlogView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

class SingleBlogView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers