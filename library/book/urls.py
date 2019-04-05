from django.urls import path

from . import views

app_name='book'
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('list', views.BookListView.as_view(), name='list'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='detail'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete'),
    path('upload', views.FileFieldView.as_view(), name='upload'),
]