from django.urls import path
from . import views

from store.controller import authview
urlpatterns = [
    path("",views.home,name="home"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('dashboard/<slug>',views.dashboardview, name="dashboardview"),
    path('dashboard/<group_slug>/<branch_slug>', views.branchview, name='branchview'),
    path('searchbranch',views.searchbranch, name="searchbranch"),
    path('register/',authview.register, name="register"),
    path('login/',authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name="logout"),
    path('Student_Report/', views.studentReportPage, name="studentReport"),

]