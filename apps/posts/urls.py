from django.urls import path
from apps.posts import views


urlpatterns = [
    # path("", views.index_view, name="index-page"),
    path("", views.IndexView.as_view(), name="index-page"),
    path("contacts/", views.contacts, name="contacts-page"),
    path("about/", views.about, name="about-page"),
    # path("post/<int:pk>", views.post_detail, name="post-detail"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post-detail"),
    path("post/delete/<int:pk>", views.PostDeleteView.as_view(), name="post-delete"),
    # path("post/delete/<int:pk>", views.post_delete, name="post-delete"),
    path("post/update/<int:pk>", views.PostUpdateView.as_view(), name="post-update"),
    # path("post/update/<int:pk>", views.post_update, name="post-update"),
    path("post/create", views.PostCreateView.as_view(), name="post-create"),
    path("api/apps.posts/list", views.PostListAPIView.as_view(), name="api-post-list"),
    path("api/apps.posts/<int:id>", views.PostDetailAPIView.as_view(), name="api-post-detail"),
]

