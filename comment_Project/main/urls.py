from django.urls import path
from . import views

# app_name = 'main' #app이 여러개일 때, 어느 앱의 url name인지 헷갈리니까 URLconf에 이름공간(namespace)을 추가하자.

urlpatterns=[
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:post_id>/add_comment/create', views.comment_create, name="comment_create"),
    path('<int:delete_id>/<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:change_id>/<int:post_id>/change/', views.change, name="change"),

    # path('<int:comment_id>/<int:post_id>/update_comment/update', views.comment_update, name ='comment_update')
]