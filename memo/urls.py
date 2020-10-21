from django.urls import path
from . import views

app_name="memo"
urlpatterns = [
    path('', views.index),
    path('nameFormat/<str:name>/', views.nameCheck),
    path('emailCheck/', views.emailCheck),
    path('userIdCheck/', views.userIdCheck),
    path('passwordCheck/', views.passwordCheck),
    path('loginIdCheck/', views.loginIdCheck),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),    
    path('<str:user_id>/', views.dashboard),
    path('<str:user_id>/newmemo/', views.newMemo),
    path('<str:user_id>/<int:memo_id>/', views.viewMemo),
    path('<str:user_id>/<int:memo_id>/editmemo/', views.editMemo),
    path('<str:user_id>/<int:memo_id>/comment/',views.comment),
    path('<str:user_id>/<int:memo_id>/<int:comment_id>/deletecomm/',views.deleteComment),
    path('<str:user_id>/settings/', views.settings),
    path('<str:user_id>/profile_pic_delete/', views.profilePicDelete),
    path('<str:user_id>/<int:memo_id>/trash_from_tab/', views.moveMemoToTrash),
    path('<str:user_id>/<int:memo_id>/permanent_delete/', views.memoPermanentDelete),
    path('<str:user_id>/<int:memo_id>/move_from_tab/', views.reAssignTab),
    path('<str:user_id>/search_preview/', views.searchPreview),
    path('<str:user_id>/search/', views.search),
    path('<str:user_id>/search/<str:keyword>/', views.searchByCrumb),
    path('<str:user_id>/deleted_memos/', views.deleted),
    path('<str:user_id>/clear/', views.clear_images),
    path('<str:user_id>/clear02/', views.clear_images02),
    path('<str:user_id>/clear03/', views.clear_images03),
    path('<str:user_id>/section1_image_upload/', views.image_upload_first_section),
    path('<str:user_id>/section2_image_upload/', views.image_upload_second_section),
    path('<str:user_id>/section3_image_upload/', views.image_upload_third_section),    
    path('<str:user_id>/messages/', views.viewMessages), 
    path('<str:user_id>/<int:dm_id>/dm_delete/', views.deleteDm), 
    path('<str:user_id>/send_dm/', views.sendDm),
    path('<str:user_id>/<int:dm_id>/check_dm/', views.checkDm),
    path('dmReplyProcess/<int:parent_dm_id>/<str:reply_user_id>/reply_dm/', views.replyDm),
    path('<str:user_id>/delete_account/', views.deleteAccount),
    path('<str:user_id>/dm_fail/', views.dmFail),
    path('<str:account_id>/<str:user_id>/<int:memo_id>/memoSave/', views.memoSave),
    path('<str:account_id>/<str:user_id>/<int:memo_id>/memoUnSave/', views.memoUnSave),
    path('<str:user_id>/saved_memos/',views.savedMemo),
    path('<str:user_id>/contact/', views.contact)

]