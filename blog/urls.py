from django.urls import path

from blog.views import (create_post, post_delete, post_detail, post_list,
                        post_update, post_view)

urlpatterns = [
    path("", post_list, name="home"),
    path("create/", create_post, name="create_post"),
    path("post/<int:id>", post_detail, name="post_detail"),
    path("post/update/<int:id>", post_update, name="post_update"),
    path("post/delete/<int:id>", post_delete, name="post_delete"),
    path("post/view/<int:id>", post_view, name="post_view"),
]
