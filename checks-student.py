#checks whether the student is present or not and further checks which class is he/she?
#CSE_B is a class, checks like digital attendance
CSE_B=["sasivarman","sasi","sv","SV","mithun","shahjan","pranav","nithin","nishant","yuva pk","sree kumar","pradeep","prasanna","alam","sarvesh","udhaya","sywas","irfan","yuvan","muthu"]
name=str(input("Enter your Name: "))
if (name in CSE_B):
    print("    DATA SAVED IN DIGI-LOGBOOK!",name,"is presented today")
    print("Welcome To Class",name,"!")
    print("Enjoy your day! ")


    print("call- 044 250 250")
    print("SV PRIVATE LTd,")

else:
    print("Wrong Entry!, You might Entered Another Class?")
    print("Enter the roll number to search which class you might be?")
    n2=int(input("Last 3 Digits of Your Roll Number: "))
    if(n2<=100):
        print("CSE")
    elif(n2>101):
        print("ECE")
    elif(n2>=201):
        print("EEE")
    elif(n2>=301):
        print("MECH")
    elif(n2>=401):
        print("CIVIL")
    else:
        print("Invalid format/number, you should contact office room")
        print("call- 044 250 250")
        print("SV PRIVATE LTd,")

    
         


