from django.urls import path

from blogapp import views

urlpatterns = [
    path('',views.all_posts, name="posts"),
    path('post/<str:id>', views.post_by_id, name="post_by_id"),
    path('create/post', views.create_post, name="create_post"),
    path('update/post/<str:id>', views.update_post, name="update_post"),
    path('delete/post/<str:id>', views.delete_post, name='delete_post')
]
