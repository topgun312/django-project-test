from django.urls import path
from robots import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("add_robot/", views.AddRobotInfo.as_view(), name="add_robot"),
    path("robot_list/", views.RobotList.as_view(), name="robot_list"),
    path(
        "download_to_excel/",
        views.DownloadExcelFile.as_view(),
        name="download_to_excel",
    ),
]
