from django.urls import path
from .views import CreateUserView, LoginView, CourseListView, EnrollmentListView, UpdateAccountView

urlpatterns = [
    path('create-account/', CreateUserView.as_view(), name='create_account'),
    path('login/', LoginView.as_view(), name='login'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('enrollments/', EnrollmentListView.as_view(), name='enrollments'),
    path('update-account/<int:pk>/', UpdateAccountView.as_view(), name='update_account'),
]
