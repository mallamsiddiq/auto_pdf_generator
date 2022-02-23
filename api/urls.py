from django.urls import path
from django.views.generic import TemplateView
#This will import our view that we have already created
from .views import DocView,TranscView,RegisterView

from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    # ...
    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    

    path('register/', RegisterView.as_view()),
    path('documents/', DocView.as_view(), name='doc-api'),
    path('transactions/', TranscView.as_view(), name='TranscView-api'),
    path('login-auth/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login-auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)