from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view

from drf_yasg import openapi
from rest_framework import permissions

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
    TokenVerifyView,
)
from accounts.views import ChangePasswordView, ObtainTokenPairView, UpdateProfileView
from fraternidad import views
from accounts.views import CreateUserView
from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="Frater",
        default_version="v1",
        description="Fraternidad Agenda",
        terms_of_service="https://example.com/terms/",
        contact=openapi.Contact(email="wmjanco@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("api/login", ObtainTokenPairView.as_view(), name="login_user"),
    path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/signup", CreateUserView.as_view(), name="create_user"),
    path(
        "api/change_password/<str:pk>/",
        ChangePasswordView.as_view(),
        name="auth_change_password",
    ),
    path(
        "api/update_profile/<str:pk>/",
        UpdateProfileView.as_view(),
        name="auth_update_profile",
    ),
    path("api/agenda", include("agendas.urls")),
    path("api/frater", include("configuracion.urls")),
    path("api/auth", include("accounts.urls")),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("graphql", GraphQLView.as_view(graphiql=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
