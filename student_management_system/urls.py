from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from student_management_app import views
from student_management_system import settings
from django.views.generic.base import RedirectView
from django.conf.urls import  url
from student_management_app import views as video_views



from student_management_app import views
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('manage/', admin.site.urls),
      #icone favorito inicial
    path('', include('student_management_app.urls')),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/imagens/fav.jpeg')),
    path('VideoIndex', video_views.Index.as_view(), name='VideoIndex'),   
    path("", views.DashboardView.as_view(), name="dashboard"),

  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


