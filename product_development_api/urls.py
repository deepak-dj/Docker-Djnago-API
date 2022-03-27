from django.contrib import admin
from django.urls import path, include
from product_app import views
from rest_framework.routers import DefaultRouter

# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token

router = DefaultRouter()
router.register("api_view", views.Product_view)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name="home"),
    path("api_view/create/", views.create_view, name="create"),
    path("register/", views.register_view, name="register"),
    path("accounts/login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("api_view/update/<int:id>/", views.update_view, name="update"),
    path("api_view/delete/<int:id>/", views.delete_view, name="delete"),
    path("", include(router.urls))
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    # path('api-token-verify/', verify_jwt_token),

]
