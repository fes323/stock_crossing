from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("discount.urls")),
    path('', include("calandary.urls")),
    path('', include("statistic.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
