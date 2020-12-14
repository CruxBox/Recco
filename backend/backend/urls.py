from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Recco API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
    path('users/',include('user.urls')),
    path('watchlists/',include('watchlists.urls')),
    path('swagger/', schema_view),
]
handler500 = 'rest_framework.exceptions.server_error'
handler400 = 'rest_framework.exceptions.bad_request'
