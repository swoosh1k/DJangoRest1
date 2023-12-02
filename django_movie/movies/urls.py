from .views import *
from django.urls import path


urlpatterns = [
    path('movie/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),
    path('review/', ReviewCreateView.as_view()),
    path('rating/', AddStarRatingView.as_view()),
    path('actor/', ActorList.as_view()),
    path('actor/<int:pk>/', ActorDetail.as_view()),
    path('category/', Category_list.as_view())

]


