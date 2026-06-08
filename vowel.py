try:
    text=str(input("Enter a text: "))
    count=0
    for i in text:
        if i in "aeiouAEIOU":
            count= count+1
    print("Number of vowels:", count)
except ValueError:
    print("An error occurred.")
finally:
    print("Program ended.")      

print("This is a simple program to count the number of vowels in a given text.")      
