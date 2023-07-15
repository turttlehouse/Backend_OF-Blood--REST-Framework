from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.list),
    path('details/<str:pk>/',views.listdetails),
    path('add/',views.addlist),
    
    
    # path('delete/<str:pk>/',views.deleteuser),
    
    path('delete/<int:id>/',views.deleteuser),
     
     
    #path('update/<int:id>',views.updateuser),
    
    # path('update/<str:pk>/',views.updateuser)
    #This is path for update
    #path('update/<str:pk>', views.updateDoner),
    
    
    path('update/<str:pk>',views.updatedoner)
    
    
    
]

'''Conclusion: one / after str:pk has failed to do update 
no any other changes committed'''


