from django.urls import path

from .views import DepartmentView, DepartmentListView

urlpatterns = [
    path('', DepartmentListView.as_view()),
    path('<int:pk>', DepartmentView.as_view()),
]
