from django.urls import path, re_path
from .views import *
# from .sitemap import SpitzSitemap, SpitzTypesSitemap # StaticViewSitemap # , DynamicViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views

# sitemaps = {
#     'spitz': SpitzSitemap,
#     'spitztypes' : SpitzTypesSitemap,
#     # 'static': StaticViewSitemap
#     # 'dynamic': DynamicViewSitemap
# }

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("types/", types, name="types"),
    # path("login/", login, name="login"), 
    path("type/<int:type_id>/", show_type, name="type"),
    path("amongus", handler404, name="handler404"),
    path("robots.txt", robots),
    path('sitemap.xml', sitemaps),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', register, name='register'),
]

handler404 = 'spitz.views.handler404'





