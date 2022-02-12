"""ProjectManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('admin/', admin.site.urls),
path('api/task/', include('Task.urls'),name="task api update status"),          
path('api/project/', include('Project.urls')),
path('api/step/', include('Step.urls')),
path('api/financial/', include('Financial.urls')),
path('user/',include('AddUser.urls')),
path('Api/',include('Api.urls')),
path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'Project.views.handler404'
handler500 = 'Project.views.handler500'
handler403 = 'Project.views.handler403'
# handler400 = 'myappname.views.error_400'



admin.site.site_header = 'پنل مدیریت پروژه'
admin.site.site_title = 'پنل مدیریت '
admin.site.index_title = " "
