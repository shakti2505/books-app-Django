from django.urls import path, include
from books.api import views
from rest_framework.routers import DefaultRouter


router  = DefaultRouter()
router.register('bookdatabase',views.BookViewSet, basename='book')


urlpatterns = [
    path('', include(router.urls))
]
