
from django.urls import path
from app_capfootball import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin', views.admin),
    path('login', views.login, name='login'),
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
