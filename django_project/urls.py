from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # Pre-built django view for user authentication
from django.urls import path,include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), # This will redirect the default home view to the home view of the blog home
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),  # Class based view
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),  # Specify where to look for the template this url points to
    path('register/',user_views.register, name = 'register'),
    path('profile/',user_views.profile, name = 'profile'),
]

if settings.DEBUG: # From the django documentation on how to serve static files supplied by the user
# https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
