from django.urls import path

from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = 'Snippets API',
        default_version = 'v1',
        description='Test description',
    )
)

app_name = 'movies'
urlpatterns = [
    path('genre/', views.genre_index, name='genre'),
    path('genre/<int:genre_pk>/', views.genre_detail, name='genre_detail'),
    path('movies/', views.movie_index, name='movie'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('movies/<int:movie_pk>/reviews/', views.reviews, name='reviews'),
    path('reviews/<int:review_pk>/', views.review_update_delete, name='review_update_delete'),
]

