from django.urls import path
from .views import PredView

urlpatterns = [
    path('', PredView.as_view(), name='index'),
]

# 画像をアップロードするたびファルダにurlと画像が保存されるようにするには以下を追加
# from django.conf import settings
# from django.conf.urls.static import static

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
