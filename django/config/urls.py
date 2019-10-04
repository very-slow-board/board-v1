from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='엄청 느린 게시판') # api doc

urlpatterns = [
    path('admin/', admin.site.urls),
]

# api
urlpatterns += [
    path('api/boards/', include('boards.urls')),
]

if settings.DEBUG:
    # api 문서화 lib
    urlpatterns += [
        path('docs/', schema_view),
    ]
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
