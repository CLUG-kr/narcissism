from django.contrib import admin
from django.urls import path
from . import views

app_name = "purchases"
urlpatterns = [
    path("<int:pk>/", views.PurchaseDetailView.as_view(), name="purchase"),
    path("create_m/", views.CreateMaterialView.as_view(), name="create_m"),
    path("create_i/", views.CreateImmaterialView.as_view(), name="create_i"),
    path("material/<int:pk>/", views.MaterialDetailView.as_view(), name="material"),
    path(
        "immaterial/<int:pk>/", views.ImmaterialDetailView.as_view(), name="immaterial"
    ),
    path(
        "material/include/<int:pk>/", views.material_attend_view, name="material-attend"
    ),
    path(
        "material/delete/<int:pk>", views.material_delete_view, name="material-delete"
    ),
    path(
        "immaterial/include/<int:pk>/",
        views.immaterial_attend_view,
        name="immaterial-attend",
    ),
    path(
        "immaterial/delete/<int:pk>/",
        views.immaterial_delete_view,
        name="immaterial-delete",
    ),
    path("search/", views.SearchView.as_view(), name="search"),
    path("delete/<int:pk>/", views.purchase_delete_view, name="delete"),
    path(
        "material/edit/<int:pk>/",
        views.EditMaterialView.as_view(),
        name="material-edit",
    ),
    path(
        "immaterial/edit/<int:pk>",
        views.EditImmaterialView.as_view(),
        name="immaterial-edit",
    ),
    path("photo/delete/<int:pk>", views.delete_photo_view, name="photo-delete"),
    path("material/close/<int:pk>", views.material_close_view, name="material-close"),
    path(
        "immaterial/close/<int:pk>",
        views.immaterial_close_view,
        name="immaterial-close",
    ),
]
