from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from .views import ProjectDetile
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('<int:pk>', ProjectDetile.as_view()),
]
