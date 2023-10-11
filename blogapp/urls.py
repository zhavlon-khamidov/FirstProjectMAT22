from django.urls import path

from blogapp import views

urlpatterns = [
    path('',views.all_posts),
    path('post/<str:id>', views.post_by_id, name="post_by_id")
]
