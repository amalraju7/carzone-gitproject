from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('packages', views.packages, name='packages'),
    path('<int:id>', views.card, name='card'),
    path('payment', views.payment, name='payment'),
    path('report', views.report, name='report'),
    path('generate', views.generate, name='generate'),
    path('generatep', views.generatep, name='generatep'),
    path('generateu', views.generatep, name='generatep'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('delete_event/<int:event_id>',views.delete_event,name='delete-event'),
]
