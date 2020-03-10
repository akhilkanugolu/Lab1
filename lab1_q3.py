
# Person Class
class Person():
#defined constructor
    def __init__(self,full_name,emailadd,p_id,phn_num):
        self.Pname = full_name
        self.email = emailadd
        self.p_id = p_id
        self.pnum = phn_num
#prints name of a person
    def getfname(self):
        print("Name : ", self.Pname)
#prints phone number
    def getphnum(self):
        print("Phone number : ", self.pnum)
#prints email address
    def getemail(self):
        print("Person email address : ", self.email)
# defined private member
    def __get_id(self):
        print("Person ID :", self.p_id)
        
class Department():
# Defined __init__ constructor   
    def __init__(self,dept,year):
        self.dept=dept
        self.Byear=year
#prints Department
    def getdept(self):
        print("Department :",self.dept)
#prints Batch Year
    def getyear(self):
        print("Batch Year :",self.Byear)

# Defined Book Details
class Book():
# Defined __init__ constructor
    def __init__(self,Book_name):
        from datetime import date,timedelta
        Booklist=["Book1","Book2","Book3"]
        BookAuthlist=["Auth1","Auth2","Auth3"]
        BookGenre=["Genre1","Genre2","Genre3"]
        self.Bname = Book_name
        if self.Bname in Booklist:
            X=input("Book is Available--Do you want to proceed Yes-Y or No-N:").upper()
            if X==('Y'):     
                self.idate = date.today()
                self.rdate = date.today()+timedelta(days=15)
                self.Bauth = BookAuthlist[Booklist.index(self.Bname)]
                self.Bgenre = BookGenre[Booklist.index(self.Bname)]
                self.getbookname()
                self.getissueddate()
                self.getreturndate()
            else:
                print("Your Booking is Cancelled")

        else:
            print("Book Not Available")
    #print book name
    def getbookname(self):
        print("Book Name :", self.Bname)
    #print author of the book
    def getbookauth(self):
        print("Author of the book :", self.Bauth)
    #print Book Genre
    def getbookgenre(self):
        print("Book Genre :", self.Bgenre)
    # print Book issued date
    def getissueddate(self):
        print("Book issued on :",self.idate)
    # print Book returned date
    def getreturndate(self):
        print("Book should be returned on :",self.rdate)
        
# Multiple inheritance, Faculty Class inherits Person,Department,Book

class Faculty(Person,Department,Book):
    def __init__(self,full_name,emailadd,p_id,phn_num,dept,year,Book_name):
        self.getprofession()
        super().__init__(full_name,emailadd,p_id,phn_num)
        Department.__init__(self,dept,year)
        Book.__init__(self,Book_name)
    
    def getprofession(self):
        print("Welcome UMKC Faculty")

# Multiple inheritance, Student Class inherits Person,Department,Book
class Student(Person,Department,Book):
    def __init__(self,full_name,emailadd,p_id,phn_num,dept,year,Book_name):
        self.getprofession()
        super().__init__(full_name,emailadd,p_id,phn_num)
        Department.__init__(self,dept,year)
        Book.__init__(self,Book_name)

    #Method OverRidding
    def getprofession(self):
        print("Welcome UMKC Student")

stud1 = Student("Akhil Teja Kanugolu","akhil@gmail.com","16297766","9842456635","ECE","2014-18","Book2")
stud1.getprofession()
print("################# Student Details  ###########################")
stud1.getfname()
stud1.getemail()
stud1.getphnum()
print("################# Department Details  #######################")
stud1.getdept()
stud1.getyear()      
print("################# Book Details  #############################")
stud1.getbookname()
stud1.getbookauth()
stud1.getbookgenre()
print("################ Book Issuing Details : #####################")
stud1.getissueddate()
stud1.getreturndate()


fac1 = Faculty("Geetanjali Makineni","geeta@gmail.com","16290659","8164420251","CSE","2001-18","Book1")
fac1.getprofession()
print("################# Faculty Details  ###########################")
fac1.getfname()
fac1.getemail()
fac1.getphnum()
print("################# Department Details  #######################")
stud1.getdept()
stud1.getyear()      
print("################# Book Details  #############################")
fac1.getbookname()
fac1.getbookauth()
fac1.getbookgenre()
print("################ Book Issuing Details : #####################")
fac1.getissueddate()
fac1.getreturndate()


