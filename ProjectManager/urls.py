from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
path('admin/', admin.site.urls),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/task/', include('Task.urls'),name="task api update status"),
path('api/financials/', include('Financial.urls')),
path('api/projects/', include('Project.urls')),
path('api/project/', include('Task.urls')),
path('api/step/', include('Step.urls')),
path('user/',include('AddUser.urls')),
path('Api/',include('Api.urls')),
path('',include('base.urls')),

path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'Project.views.handler404'
handler500 = 'Project.views.handler500'
handler403 = 'Project.views.handler403'

admin.site.site_header = 'پنل مدیریت پروژه'
admin.site.site_title = 'پنل مدیریت '
admin.site.index_title = " "
