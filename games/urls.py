from django.urls import path

from . import views

urlpatterns = [
    path('online-games/', views.online_game, name='oneline_games'),
    path('sum/<int:num1>/<int:num2>/', views.get_addition_number, name='addition'),
    path('addition/', views.addition_numbers, name='addition'),
    path('substract/', views.substract_number, name='substract'),
    path('login/', views.login, name='login'),
    path('login/class/', views.LoginView.as_view(), name='login'),
    path('str_count', views.StrCount.as_view(), name='login'),
    path('school', views.AddSchool.as_view(), name='login'),
    path('school/<int:school_id>', views.UpdateSchool.as_view(), name='login'),
    path('school/<int:school_id>/course', views.AddCourses.as_view(), name='login'),
]




# /games/school -- Post (Add school)
#               -- GET (Fetch all schools)



# /games/school/<school_id> -- PUT (Update school name or address)
#                           -- DELETE (Remove the school info from database)


# /games/school/<school_id>/course -- POST
#                                  -- GET