from django.urls import path
from . import views 

app_name = "members"


urlpatterns = [
    path("", views.index, name="members" ),
    path("post/<str:post_id>", views.detail, name= "detail"),
    path("pages", views.page, name= "pages"),
    path("new_something_url", views.new_url_views, name="new_page_url"),
    path("old_url", views.old_url_redirect, name="old_url")
]