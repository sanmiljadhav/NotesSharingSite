from django.urls import path
from Notes import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name = 'notes-index'),
    path('about/',views.about,name = 'notes-about'),
    path('contact/',views.contact,name='notes-contact'),
    path('login/',views.userlogin,name='notes-login'),
    path('login_admin/',views.login_admin,name='notes-admin_login'),
    path('admin_page/',views.admin_page,name = 'notes-admin_page'),
    path('register/',views.register,name='notes-register'),
    path('logout/',views.logout_admin,name='logout'),
    path('userprofile/',views.userprofile,name = 'userprofile'),
    path('changepassword/',views.changepassword,name = 'changepassword'),
    path('editprofile/',views.editprofile,name = 'editprofile'),
    path('uploadnotes/',views.uploadnotes,name = 'uploadnotes'),
    path('viewmynotes/',views.viewmynotes,name = 'viewmynotes'),
    path('deletemynotes/<int:pid>',views.deletemynotes,name = 'deletemynotes'),
    path('admin_viewusers',views.admin_viewusers,name = 'admin_viewusers'),
    path('admin_delete_user/<int:pid>',views.admin_delete_user,name = 'admin_delete_user'),
    path('pending_notes',views.pending_notes,name= 'pending_notes'),
    path('assign_status/<int:pid>',views.assign_status,name = 'assign_status'),
    path('accepted_notes/',views.accepted_notes,name = 'accepted_notes'),
    path('rejected_notes/',views.rejected_notes,name = 'rejected_notes'),
    path('all_notes/',views.all_notes,name = 'all_notes'),
    path('admin_delete_notes/<int:pid>',views.admin_delete_notes,name = 'admin_delete_notes'),
    path('user_all_notes',views.user_all_notes,name = 'user_all_notes'),


]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
#Whenever we are uploading file write this 