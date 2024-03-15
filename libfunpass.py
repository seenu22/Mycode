def border(n):
    for i in range (1,n+1):
        print("-",end=" ")
    print()
l=['python','c','java','html']
b_l=[]
tb_b=[]
std_id=int(input("Entr the student id :"))
name=input("Enter the name :")
dept=input("Enter the department name :")

def l_books(l):
    border(20)
    print("List of books")
    border(20)
    print(l)

def b_books(l,b_l,tb_b,std_id):
    border(20)
    id=int(input("Enter the studend id :"))
    border(20)
    if id == std_id:
        s=input("Enter the book name :")
        if s in l:
            print("The search book is available in the library")
            b_l.append(s)
            tb_b.append(s)
            l.remove(s)
            print("*****The book is barrow successfully*****")
        else:
            print("The book is not available")
    else:
        print("The student id is mismatch")


def r_books(std_id,l,b_l):
    id=int(input("Enter the student id :"))
    if id == std_id:
        bn=input("Enter the barrowed book name :")
        if bn in b_l:
            l.append(bn)
            b_l.remove(bn)
            print("****The book is returned successfully****")
        else:
            print("You can not barrow this book ")
    else:
        print("The id is mismatch")


def details(name,std_id,b_l,tb_b,dept):
    id=int(input("Enter the student id :"))
    if id == std_id:

        print("The student details")
        print("Student name :",name)
        print("department name :",dept)
        print("Student id :",std_id)
        print("barrowed books :",b_l)
        print("Total barrowed books :",tb_b)
    else:
        print("mismatch id")

        
msg="""1.list books
2.barrow book
3.return book
4.details
5.exit"""
while True:
    print(msg)
    c=int(input("select the choice :"))
    if c==1:
        l_books(l)
    elif c==2:
        b_books(l,b_l,tb_b,std_id)
    elif c==3:
        r_books(std_id,l,b_l)
    elif c==4:
        details(name,std_id,b_l,tb_b,dept)
    elif c==5:
        break