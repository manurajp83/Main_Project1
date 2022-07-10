from django.db import models
class category(models.Model):
    cat_id=models.CharField(max_length=30)
    cat_name=models.CharField(max_length=30)
    photo=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="category"
# Create your models here.
class product(models.Model):
    product_id=models.CharField(primary_key=True, max_length=30)
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    model=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    stockquantity=models.CharField(max_length=30)
    photo=models.CharField(max_length=100)
    remark=models.CharField(max_length=100)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="product"




class jobmaster(models.Model):
    jobid=models.CharField(primary_key=True, max_length=30)
    jobname=models.CharField(max_length=30)
    salary=models.IntegerField()
    TA=models.IntegerField()
    DA=models.IntegerField()
    HRA=models.IntegerField()
    LIC=models.IntegerField()
    PF=models.IntegerField()
    welfare=models.IntegerField()
    class Meta:
        db_table="jobmaster"

class tbl_vacancy(models.Model):
    vacancy_id=models.CharField(primary_key=True, max_length=30)
    jobid=models.ForeignKey(jobmaster, on_delete=models.CASCADE)
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    numberofvacancy=models.CharField(max_length=30)
    application_lastdate=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_vacancy"


class jobapplication(models.Model):
    name=models.CharField(max_length=30)
    vacancy_number=models.IntegerField()
    job_name=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    nature_of_experience=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    photo=models.CharField(max_length=50)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="jobapplication"


class login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    type1=models.CharField(max_length=30)
    class Meta:
        db_table="login"


class staffnew1(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=30)
    name=models.CharField(max_length=30)
    jobid=models.ForeignKey(jobmaster, on_delete=models.CASCADE)
    date_of_join=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    photo=models.CharField(max_length=100)
    basic_salalary=models.IntegerField()
    remark=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="staffnew1"



class duty(models.Model):
    dutyid= models.CharField(primary_key=True, max_length=30)
    staff_id=models.ForeignKey(staffnew1, on_delete=models.CASCADE)
    jobdescription=models.CharField(max_length=30)
    section=models.CharField(max_length=30)
    allotmentdate=models.CharField(max_length=30)
    class Meta:
        db_table="duty"

class jobapply(models.Model):
    application_id= models.CharField(primary_key=True, max_length=30)
    vacancy_id=models.ForeignKey(tbl_vacancy, on_delete=models.CASCADE)
    applicant_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    dob=models.CharField(max_length=30)
    qualification=models.CharField(max_length=30)
    experience=models.CharField(max_length=30)
    experience_history=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    application_date=models.CharField(max_length=30)
    remark=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="jobapply"


class tbl_idgen(models.Model):
    sid = models.IntegerField()
    duid = models.IntegerField()
    rid = models.IntegerField()
    slid = models.IntegerField()
    prid = models.IntegerField()
    pid = models.IntegerField()
    jid = models.IntegerField()
    vid = models.IntegerField()
    aid = models.IntegerField()
    lid = models.IntegerField()
    class Meta:
        db_table = "tbl_idgen"


class rawmaterial(models.Model):
    materialid= models.CharField(primary_key=True, max_length=30)
    description=models.CharField(max_length=30)
    materialname=models.CharField(max_length=30)
    stock=models.IntegerField()
    rol=models.IntegerField()
    class Meta:
        db_table="rawmaterial"   
class supplier(models.Model):
    supplierid = models.CharField(primary_key=True, max_length=30)
    materialid=models.ForeignKey(rawmaterial, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=30)
    remark=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="supplier"
class purchaseorder(models.Model):
    purchaseorderid = models.CharField(primary_key=True, max_length=30)
    materialid=models.ForeignKey(rawmaterial, on_delete=models.CASCADE)
    supplierid=models.ForeignKey(supplier, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    requirements=models.CharField(max_length=100)
    orderdate=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    class Meta:
        db_table="purchaseorder"        
class tbl_leave(models.Model):
    Leave_id= models.CharField(primary_key=True, max_length=30)
    staff_id = models.ForeignKey(staffnew1, on_delete=models.CASCADE)
    numberofdays=models.CharField(max_length=30)
    application_date=models.CharField(max_length=30)
    reason=models.CharField(max_length=30)
    status=models.CharField(max_length=30)
    class Meta:
        db_table="tbl_leave"
