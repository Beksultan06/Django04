from django.urls import path
from posts import views


urlpatterns = [
    path("", views.index_view, name="index-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page"),
    path("post/<int:pk>", views.post_detail, name="post-detail"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post-delete')
]