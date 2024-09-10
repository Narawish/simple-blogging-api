from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.BlogView.as_view()),
    path('blog/<int:pk>', views.SingleBlogView.as_view()),

]
