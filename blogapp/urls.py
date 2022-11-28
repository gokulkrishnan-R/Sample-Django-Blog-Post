from django.urls import path
from.import views

urlpatterns=[

    path("",views.home,name="home"),
    path("posts/",views.posts,name="posts"),
    path("posts/newpost/",views.newpost,name="newpost"),
    path("posts/newpost/newpostrecord/",views.newpostrecord,name="newpostrecord"),
    path("about/",views.about,name="about"),
    path("posts/delete/<int:id>",views.delete,name="delete"),
    path("posts/update/<int:id>",views.update,name="update"),
    path("posts/update/updaterecord/<int:id>",views.updaterecord,name="updaterecord"),
    path("search/",views.search,name="search"),
    path("posts/login_user/",views.login_user,name="login_user"),

    #user authentication
    path("register/", views.Register, name="register"),
    path("login/",views.Login,name="login"),
    path("logout/", views.Logout, name="logout"),

    #comments
    
    path("posts/user_comments/<int:id>/",views.user_comments,name="user_comments"),
    #path("posts/add_user_comments/<int:id>/add_user_comments/",views.add_user_comments,name="add_user_comments"),        
]