from django.urls import path ,include
from Credicxo import views
# from Credicxo.views import MyObtainTokenPairView
# from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('',views.Student_list),
    path('student/<int:pk>',views.Student_details),
]
