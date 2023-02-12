from django.urls import path
from .views import (PostList,
                    PostDetail,
                    PostSearch,
                    NewsCreate,
                    ArticlesCreate,
                    NewsUpdate,
                    ArticlesUpdate,
                    NewsDelete,
                    ArticlesDelete)


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('articlecreate/', ArticlesCreate.as_view(), name='articles_create'),
   path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
   path('<int:pk>/articleupdate/', ArticlesUpdate.as_view(), name='articles_update'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   path('<int:pk>/articledelete/', ArticlesDelete.as_view(), name='articles_delete'),
]
