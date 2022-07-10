from django.shortcuts import render,redirect
from app1.models import category, supplier
from app1.models import product,tbl_vacancy,login,tbl_leave,staffnew1,tbl_idgen,duty,rawmaterial,purchaseorder,jobmaster,jobapply
from django.core.files.storage import FileSystemStorage
import datetime

def index(request):
    return render(request,'index.html')  
def admin(request):
    return render(request,'admin.html')    
def category1(request):
    return render(request,'category.html')  
def insertion(request):
    if request.method=='POST':
       data=category()
       data.cat_id="na"
       data.cat_name=request.POST.get('cat_name')
       photo=request.FILES['photo']
       fs=FileSystemStorage()
       Filename=fs.save(photo.name,photo)
       uploaded_file_url=fs.url(Filename)
       data.photo=uploaded_file_url
       data.status="ok"
       data.save()
       data.cat_id="category"+str(data.id)
       data.save()
       return render(request,'category.html') 

def viewdata(request):
    items=category.objects.all()
    return render(request,"removecategory.html",{'item':items})  

def delete(request,id):
    d=category.objects.get(id=id)
    d.delete()
    return redirect('/viewdata')
def product1(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.pid
    id = int(id+1)
    pid = "PRODUCT_00" + str(id)
    request.session["pid"] = id
    request.session["pid1"] = pid

    data=category.objects.all()
    return render(request,'product.html',{'data':data})
def insertion1(request):
    if request.method == 'POST':
       data=product()
       data.product_id=request.session["pid1"]
       data.category=request.POST.get('category')
       data.name=request.POST.get('name')
       data.size=request.POST.get('size')
       data.description=request.POST.get('description')
       data.price=request.POST.get('price')
       data.color=request.POST.get('color')
       data.model=request.POST.get('model')
       data.stockquantity=request.POST.get('stockquantity')
       photo=request.FILES['photo']
       fs=FileSystemStorage()
       Filename=fs.save(photo.name,photo)
       uploaded_file_url=fs.url(Filename)
       data.photo=uploaded_file_url
       data.remark=request.POST.get('remark')
       data.save()  
       data2=tbl_idgen.objects.get(id=1)
       data2.pid=request.session['pid']
       data2.save()
       return render(request,'admin.html')
  
def staff(request):
    data=jobmaster.objects.all()
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.sid
    id = int(id+1)
    sid = "STAFF_00" + str(id)
    request.session["sid"] = id
    request.session["sid1"] = sid
    return render(request,'staffs.html',{'vac':data})        

def viewdata1(request):
    items=product.objects.all()
    return render(request,"removeproduct.html",{'item':items})

def viewdata2(request):
    items=product.objects.all()
    return render(request,"viewdata2.html",{'item':items})  

def delete2(request,id):
    d=product.objects.get(product_id=id)
    d.delete()
    return redirect('/viewdata1')

def staffinsertion(request):
        if request.method == 'POST':  
            c=staffnew1()
            c.staff_id=request.session["sid1"]
            c.name=request.POST.get('name')
            c.jobid_id=request.POST.get('designation')
            c.date_of_join=request.POST.get('date_of_join')
            c.qualification=request.POST.get('qualification')
            c.experience=request.POST.get('experience')
            c.address=request.POST.get('address')                 
            c.phone=request.POST.get('phone')
            c.email=request.POST.get('email')
            c.basic_salalary=request.POST.get('basic_salary')
            c.remark="NULL"
            c.status="OK"
            c.save()
            data1=tbl_idgen.objects.get(id=1)
            data1.sid=request.session['sid']
            data1.save()
            data3=login()
            data3.username=request.session["sid1"]
            data3.password=request.POST.get('phone')
            data3.type1="staff"
            data3.save()
            return render(request,'admin.html')

def log(request):
    return render(request,'logins.html')
def loginprocess(request):
    if request.method=='POST':
     log=login.objects.all()
     username=request.POST.get('username') 
     password=request.POST.get('password')
     flag=0
     ty=''
     for r in log:
         if r.username==username and r.password==password:
             
             flag=1
             ty=r.type1
    
    if flag==1:
        if ty=='admin':
            request.session['admin']=username
            return render(request,'admin.html') 
        elif ty=='staff':   
            request.session['staff']=username
            return render(request,'staff.html') 
        elif ty=='dealer':
            return render(request,'dealer.html')
        elif ty=='supplier':
            request.session['supplier']=username
            return render(request,'supplierhome.html')  
        elif ty=='staff':
            return render(request,'staff.html')         
    else:
        return render(request,'logins.html')  

def stafflogout(request):
    del request.session['staff']
    return render(request,"index.html")

def supplierlogout(request):
    del request.session['supplier']
    return render(request,"index.html")

def adminhome(request):
    return redirect(request,"admin.html")
def adminlogout(request):
    del request.session['admin']
    return render(request,"index.html")
def allotduty(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.duid
    id = int(id+1)
    duid = "DUTY_00" + str(id)
    request.session["duid"] = id
    request.session["duid1"] = duid
    data3=staffnew1.objects.all()
    return render(request,"duty.html",{'data3':data3})    
def duty1(request):    
    if request.method == 'POST':  
            c=duty()
            c.dutyid=request.session["duid1"]
            c.staff_id_id=request.POST.get('staff_id')
            c.section=request.POST.get('section')
            c.jobdescription=request.POST.get('description')
            c.allotmentdate=datetime.datetime.now().strftime ("%Y-%m-%d")

            
            c.save()
            data1=tbl_idgen.objects.get(id=1)
            data1.duid=request.session['duid']
            data1.save()
            return render(request,'admin.html')
           

def addmaterial(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.rid
    id = int(id+1)
    rid = "MATERIAL_00" + str(id)
    request.session["rid"] = id
    request.session["rid1"] = rid
    return render(request,"addmaterial.html")    
def addmaterial1(request):    
    if request.method == 'POST':  
            c=rawmaterial()
            c.materialid=request.session["rid1"]
            c.materialname=request.POST.get('name')
            c.description=request.POST.get('description')
            c.stock=request.POST.get('stock')
            c.rol=request.POST.get('rol')        
            c.save()

            data1=tbl_idgen.objects.get(id=1)
            data1.rid=request.session['rid']
            data1.save()
            return render(request,'admin.html')   
def removematerial(request):
    items=rawmaterial.objects.all()
    return render(request,"removematerial.html",{'item':items})            
def removematerial1(request,id):
    items=rawmaterial.objects.get(materialid=id)
    items.delete()
    return redirect('/removematerial')         
def viewmaterial(request):
    items=rawmaterial.objects.all()
    return render(request,"viewmaterial.html",{'item':items})   
    
def addsupplier(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.slid
    id = int(id+1)
    slid = "SUPPLIER_00" + str(id)
    request.session["slid"] = id
    request.session["slid1"] = slid
    data3=rawmaterial.objects.all()
    return render(request,'addsupplier.html',{'data3':data3})        
                  
def addsupplier1(request):
        if request.method == 'POST':  
            c=supplier()
            c.supplierid=request.session["slid1"]
            c.materialid_id=request.POST.get('materialid')
            c.name=request.POST.get('name')
            
            c.address=request.POST.get('address')                 
            c.phone=request.POST.get('phone')
            c.email=request.POST.get('email')
            c.remark=request.POST.get('remark')
            c.status="verified"
            c.save()
            data3=login()
            data3.username=request.session["slid1"]
            data3.password=request.POST.get('phone')
            data3.type1="supplier"
            data3.save()
            data1=tbl_idgen.objects.get(id=1)
            data1.slid=request.session['slid']
            data1.save()
            return render(request,'admin.html')
       

def removesupplier(request):
    items=supplier.objects.all()
    return render(request,"removesupplier.html",{'item':items})   
def supplierv(request):
    items=supplier.objects.filter(status="notverified")
    return render(request,"supplier.html",{'item':items})              
def removesupplier1(request,id):
    items=supplier.objects.get(supplierid=id)
    items.delete()
    return redirect('/removesupplier') 
def verifysupplier(request,id):
    items=supplier.objects.get(supplierid=id)
    items.status="verified"
    items.save()
    data3=login()
    data3.username=items.supplierid
    data3.password=items.phone
    data3.type1="supplier"
    data3.save()
    return redirect('/supplier')         
def updatematerialstock(request):
    data3=rawmaterial.objects.all() 
    return render(request,"updatematerialstock.html",{'data3':data3})
def updatematerialstock1(request):
    data3=rawmaterial.objects.get(materialid=request.POST.get('materialid'))
    s=int(request.POST.get('stock'))
    s1=int(data3.stock)
    newstock=s1-s
    data3.stock=newstock
    data3.save()
    r=int(data3.rol)
    if newstock<=r:
        data1 = tbl_idgen.objects.get(id=1)
        id = data1.prid
        id = int(id+1)
        prid = "PURCHASE ORDER_00" + str(id)
        request.session["prid"] = id
        request.session["prid1"] = prid
        data=supplier.objects.filter(materialid=data3.materialid)
        return render(request,"purchaseorder.html",{'m':data3.materialid,'data':data})
    return render(request,"staff.html")    
def purchaseorder1(request):    
    if request.method == 'POST':  
            c=purchaseorder()
            c.purchaseorderid=request.session["prid1"]
            c.materialid_id=request.POST.get('materialid')
            c.supplierid_id=request.POST.get('supplierid')
            c.requirements=request.POST.get('requirement')
            c.quantity=request.POST.get('quantity') 
            c.orderdate=datetime.datetime.now().strftime ("%Y-%m-%d")
            c.status="pending"
            c.month=request.POST.get('month')
            c.year=request.POST.get('year')
            c.save()
            
            data1=tbl_idgen.objects.get(id=1)
            data1.prid=request.session['prid']
            data1.save()
            return render(request,'staff.html')
def updateproductstock(request):
    data3=product.objects.all() 
    return render(request,"updateproductstock.html",{'data3':data3})
def updateproductstock1(request):
    data3=product.objects.get(product_id=request.POST.get('productid'))
    s=int(request.POST.get('stock'))
    s1=int(data3.stockquantity)
    newstock=s1+s
    data3.stockquantity=newstock
    data3.save()
    return render(request,"staff.html")        
def generatepurchaseorder(request):
    data3=purchaseorder.objects.all() 
    return render(request,"generatepurchaseorder.html",{'data3':data3})            

# Create your views here.
def supreg(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.slid
    id = int(id+1)
    slid = "SUPPLIER_00" + str(id)
    request.session["slid"] = id
    request.session["slid1"] = slid
    data3=rawmaterial.objects.all()
    return render(request,'supreg.html',{'data3':data3})        
                  

def supreg1(request):
    if request.method == 'POST':  
        c=supplier()
        c.supplierid=request.session["slid1"]
        c.materialid_id=request.POST.get('materialid')
        c.name=request.POST.get('name')
        c.address=request.POST.get('address')                 
        c.phone=request.POST.get('phone')
        c.email=request.POST.get('email')
        c.remark=request.POST.get('remark')
        c.status="notverified"
        c.save()
        data1=tbl_idgen.objects.get(id=1)
        data1.slid=request.session['slid']
        data1.save()
        return render(request,'index.html')

def addjob(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.jid
    id = int(id+1)
    jid = "JOB_00" + str(id)
    request.session["jid"] = id
    request.session["jid1"] = jid
    return render(request,'addjob.html')

def addjob1(request):    
    if request.method == 'POST':  
            c=jobmaster()
            c.jobid=request.session["jid1"]
            c.jobname=request.POST.get('jobname')
            c.salary=int(request.POST.get("salary"))
            s=int(request.POST.get("salary"))
            c.TA=int(s*9/100)
            c.DA=int(s*13/100)
            c.HRA=int(s*20/100)
            c.LIC=int(s*9/100)
            c.PF=int(s*12/100)
            c.welfare=int(s*10/100)
            c.save()

            data1=tbl_idgen.objects.get(id=1)
            data1.jid=request.session['jid']
            data1.save()
            return render(request,'admin.html')   
def removejob(request):
    items=jobmaster.objects.all()
    return render(request,"removejob.html",{'item':items})            
def removejob1(request,id):
    items=jobmaster.objects.get(jobid=id)
    items.delete()
    return redirect('/removejob')

def addvacancy(request):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.vid
    id = int(id+1)
    vid = "VAC_00" + str(id)
    request.session["vid"] = id
    request.session["vid1"] = vid

    data=jobmaster.objects.all()
    return render(request,'addvacancy.html',{'data1':data})
def addvacancy1(request):
    if request.method == 'POST':
        c=tbl_vacancy()
        c.vacancy_id=request.session["vid1"]
        c.jobid_id=request.POST.get('jobname')
        c.qualification=request.POST.get('qualification')
        c.experience=request.POST.get('experience')
        c.numberofvacancy=request.POST.get('numberofvacancy')
        c.application_lastdate=request.POST.get('application_lastdate')
        c.status="NP"
        c.save()

        data1=tbl_idgen.objects.get(id=1)
        data1.vid=request.session['vid']
        data1.save()
        return render(request,'admin.html')   

def removevacancy(request):
    items=tbl_vacancy.objects.all()
    return render(request,"removevacancy.html",{'item':items})            
def removevacancy1(request,id):
    items=tbl_vacancy.objects.get(vacancy_id=id)
    items.delete()
    return redirect('/removevacancy')

def viewjob(request):
    items=jobmaster.objects.all()
    return render(request,"viewjob.html",{'item':items})  

def viewvacancy(request,id):
    data=tbl_vacancy.objects.filter(jobid=id)
    return render(request,"viewvacancy.html",{'data':data})


def applyjob1(request,id1):
    data1 = tbl_idgen.objects.get(id=1)
    id = data1.aid
    id = int(id+1)
    aid = "APPL_00" + str(id)
    request.session["aid"] = id
    request.session["aid1"] = aid
    
    data=tbl_vacancy.objects.get(vacancy_id=id1)
    return render(request,"apply.html",{'data':data})

def applyjob(request):
    if request.method=='POST':
        c=jobapply()
        c.application_id=request.session["aid1"]
        c.vacancy_id_id=request.POST.get('vacancyid')
        c.applicant_name=request.POST.get('applicantname')
        c.address=request.POST.get('address')
        c.gender=request.POST.get('gender')
        c.dob=request.POST.get('dob')
        c.qualification=request.POST.get('qualification')
        c.experience=request.POST.get('experience')
        c.experience_history=request.POST.get('experiencehistory')
        c.phone=request.POST.get('phone')
        c.email=request.POST.get('email')
        c.application_date=datetime.date.today()
        c.status="Pending"
        c.save()

        data1=tbl_idgen.objects.get(id=1)
        data1.aid=request.session['aid']
        data1.save()
        return render(request,'index.html')

def viewjob1(request):
    items=jobmaster.objects.all()
    return render(request,"viewjob1.html",{'item':items})  

def viewvacancy1(request,id):
    data=tbl_vacancy.objects.filter(jobid=id)
    return render(request,"viewvacancy1.html",{'data':data})

def viewapplication(request,id):
    data=jobapply.objects.filter(vacancy_id=id).filter(status="Pending")
    return render(request,"viewapplication.html",{'data':data})

def viewapplication1(request,id):
    data=jobapply.objects.get(application_id=id)
    data.status="Appointed"
    data.save()

    data1 = tbl_idgen.objects.get(id=1)
    id = data1.sid
    id = int(id+1)
    sid = "STAFF_00" + str(id)
    request.session["sid"] = id
    request.session["sid1"] = sid
    print(data.vacancy_id.jobid)
    return render(request,"staffnew.html",{'data1':data})

def insertstaff2(request):
    if request.method == 'POST':  
        c=staffnew1()
        c.staff_id=request.session["sid1"]
        c.name=request.POST.get('name')
        c.jobid_id=request.POST.get('designation')
        c.date_of_join=request.POST.get('date_of_join')
        c.qualification=request.POST.get('qualification')
        c.experience=request.POST.get('experience')
        c.address=request.POST.get('address')                 
        c.phone=request.POST.get('phone')
        c.email=request.POST.get('email')
        c.basic_salalary=request.POST.get('basic_salary')
        c.remark="NULL"
        c.status="OK"
        c.save()

        data1=tbl_idgen.objects.get(id=1)
        data1.sid=request.session['sid']
        data1.save()

        data3=login()
        data3.username=request.session["sid1"]
        data3.password=request.POST.get('phone')
        data3.type1="staff"
        data3.save()
        return render(request,'admin.html')

def viewstaff(request):
    items=staffnew1.objects.all()
    return render(request,"viewstaff.html",{'item':items})

def viewsalary(request,id):
    data=staffnew1.objects.get(jobid=id)
    Allowance=int(data.jobid.TA+data.jobid.DA+data.jobid.HRA)
    Reduction=int(data.jobid.PF+data.jobid.LIC+data.jobid.welfare)
    Netsalary=int((data.jobid.salary+Allowance)-Reduction)
    
    return render(request,"viewsalary.html",{'data1':data,'data2':Allowance,'data3':Reduction,'data4':Netsalary})
def applyleave(request):
    data1=staffnew1.objects.get(staff_id=request.session['staff'])

    data = tbl_idgen.objects.get(id=1)
    id = data.lid
    id = int(id+1)
    lid = "LEAVE_00" + str(id)
    request.session["lid"] = id
    request.session["lid1"] = lid
    return render(request,"applyleave.html",{'data':data1})

def applyleave1(request):
    today = datetime.date.today()
    if request.method=='POST':
        c=tbl_leave()
        c.Leave_id=request.session["lid1"]
        c.staff_id_id=request.POST.get('staffid')
        c.numberofdays=request.POST.get('numberofdays')
        c.application_date=today
        c.reason=request.POST.get('reason')
        c.status="pending"
        c.save()


        data1=tbl_idgen.objects.get(id=1)
        data1.lid=request.session['lid']
        data1.save()
        return render(request,'staff.html')

def viewstaff1(request):
    data=staffnew1.objects.all()
    return render(request,"viewstaff1.html",{'data1':data})

def viewleave(request,id):
    data=tbl_leave.objects.filter(staff_id=id).filter(status="Pending")
    return render(request,"viewleave.html",{'data':data})

def acceptleave(request,id):
    data = tbl_leave.objects.get(Leave_id=id)
    data.status = "Accepted"
    data.save()
    return redirect("/viewleave")
def rejectleave(request,id):
    data = tbl_leave.objects.get(Leave_id=id)
    data.status = "Rejected"
    data.save()
    return redirect("/viewleave")

def viewleave1(request):
    data=tbl_leave.objects.filter(staff_id=request.session['staff'])
    return render(request,"viewleave1.html",{'data1':data})

def viewstaff2(request):
    data=staffnew1.objects.all()
    return render(request,"viewstaff2.html",{'data1':data})

def viewsalary1(request,id):
    data=staffnew1.objects.get(staff_id=id)
    Allowance=int(data.jobid.TA+data.jobid.DA+data.jobid.HRA)
    Reduction=int(data.jobid.PF+data.jobid.LIC+data.jobid.welfare)
    Netsalary=int((data.jobid.salary+Allowance)-Reduction)
    
    return render(request,"viewsalary2.html",{'data1':data,'data2':Allowance,'data3':Reduction,'data4':Netsalary})

def viewrawmaterial1(request):
    items=rawmaterial.objects.all()
    return render(request,"viewrawmaterial.html",{'item':items}) 

def viewpurchaseorder1(request):
    data=purchaseorder.objects.all()
    return render(request,"viewmonth.html",{'data1':data}) 

def vieworder1(request):
    if request.method=='POST':
        s1=request.POST.get('month')
        s2=request.POST.get('year')
        data=purchaseorder.objects.filter(month=s1).filter(year=s2)
        return render(request,"vieworder.html",{'data1':data}) 

def viewapplications1(request):
    data=tbl_leave.objects.all()
    return render(request,"viewleave2.html",{'data1':data})
def search(request):   
    data = request.POST.get('search')
    # data2 = products.objects.all()
    # data5=[];  
    # data6=[];  
    # for x in data2: 
    #     p=x.name.lower()
    #     data5.append(p)
    # for y in data5:
    #     if data in y:
    #         data6.append(y)   
    # for s in data6:
    if data:
        result=product.objects.filter(name__icontains=data)
        return render(request,'viewproducts.html',{'items':result})  
    else:
        items=product.objects.all()
        return render(request,"viewproducts.html",{'items':items})    
def viewproducts(request):
    items=product.objects.all()
    return render(request,"viewproducts.html",{'items':items})








    
       