
from django.urls import path, include, reverse_lazy
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.AdListView.as_view()),
    path('ads', views.AdListView.as_view(), name='ads'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',
        views.PicFormView.as_view(success_url=reverse_lazy('ads')), name='ad_create'),
    path('ad/<int:pk>/update',
        views.PicFormView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),
    path('ad/<int:pk>/delete',
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_delete'),
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),
    path('ad/<int:pk>/comment',
        views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')), name='comment_delete'),
    path('ad/<int:pk>/favorite',
    views.AddFavoriteView.as_view(), name='ad_favorite'),
path('ad/<int:pk>/unfavorite',
    views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]