class multiplefunctions():
    def Subfields():
        subfields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in subfields:
            print(i)
    
    
    def OddEven():
        num=int(input("Enter a number: "))
        if (num %2 !=0):
            print(num,"odd number")
        else: 
            print(num,"even number")

    def eligible():
        gender=input("Your Gender: ")
        age=int(input("Your Age: "))
        if(gender=="Male"):
            if(age>21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        if(gender=="Female"):
            if(age>18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")  

    def FindPercent():
        subject1=98
        subject2=87
        subject3=95
        subject4=95
        subject5=93
        Total=subject1+subject2+subject3+subject4+subject5
        print("Subject1=",subject1)
        print("Subject2=",subject2)
        print("Subject3=",subject3)
        print("Subject4=",subject4)
        print("Subject5=",subject5)
        print("Total=",Total)
        percentage=Total/500*100
        print("Percentage=",percentage)
    
    def triangle():
        Height = 32
        Breadth = 34
        print("Height:",Height)
        print("Breadth:",Breadth)
        area_of_triangle = (Height * Breadth)/2
        print("Area formula: (Height * Breadth)/2")
        print("Area of Triangle:",area_of_triangle)
        Height1=2
        Height2=4
        Breadth=4
        print("Height1:",Height1)
        print("Height2:",Height2)
        print("Breadth:",Breadth)
        perimeter_of_triangle= Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",perimeter_of_triangle)
    


