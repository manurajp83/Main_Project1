"""VKC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path ('index/',views.index),
    path ('adminhome/',views.adminhome),
    path('viewjob/',views.viewjob),
    path('viewvacancy/<str:id>',views.viewvacancy),
    path('applyjob/<str:id1>',views.applyjob1),
    path('applyjob1/',views.applyjob),
    path('viewapplication',views.viewjob1),
    path('viewvacancy1/<str:id>',views.viewvacancy1),
    path('viewapply/<str:id>',views.viewapplication),
    path('viewapply1/<str:id>',views.viewapplication1),
    path('staffinsert1/',views.insertstaff2),

    path('viewsalary/',views.viewstaff),
    path('viewsalarystatement/<str:id>',views.viewsalary),

  
  
    path('category/',views.category1),
    path('insertion/',views.insertion),

    path('viewdata/',views.viewdata),
    path('delete/<int:id>',views.delete),

    path('product/',views.product1),
    path('insertion1/',views.insertion1),

    
    path('addjob/',views.addjob),
    path('addjob1/',views.addjob1),
    path('removejob/',views.removejob),
    path('removejob1/<str:id>',views.removejob1),
    
    path('staff/',views.staff),
   
   
    path('viewdata1/',views.viewdata1),

   

    path('viewdata2/',views.viewdata2),
    path('delete2/<int:id>',views.delete2),



    path('addvacancy/',views.addvacancy),
    path('addvacancy1/',views.addvacancy1),
    path('removevacancy/',views.removevacancy),
    path('removevacancy1/<str:id>',views.removevacancy1),

    
    path('logout/',views.stafflogout),
    path('logout1/',views.supplierlogout),
    
    path('staffinsert/',views.staffinsertion),

    path('log/',views.log),
    path('login/',views.loginprocess),

    path('allotduty/',views.allotduty),
    path('duty1/',views.duty1),

    path('adminlogout/',views.adminlogout),
    path('addmaterial/',views.addmaterial),
    path('addmaterial1/',views.addmaterial1),
    path('removematerial/',views.removematerial),
    path('removematerial1/<str:id>',views.removematerial1),
    path('addsupplier/',views.addsupplier),
    path('addsupplier1/',views.addsupplier1),
    path('removesupplier/',views.removesupplier),
    path('removesupplier1/<str:id>',views.removesupplier1),
    path('updatematerialstock/',views.updatematerialstock),
    path('updatematerialstock1/',views.updatematerialstock1),
    path('purchaseorder1/',views.purchaseorder1),
    path('updateproductstock/',views.updateproductstock),
    path('updateproductstock1/',views.updateproductstock1),
    path('generatepurchaseorder/',views.generatepurchaseorder),
    path('supreg/',views.supreg),
    path('supreg1/',views.supreg1),
    path('verifysupplier/<str:id>',views.verifysupplier),
    path('supplier/',views.supplierv),
    #path('viewcomplaints/',views.viewcomplaints),
   
  
   



    

    




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)