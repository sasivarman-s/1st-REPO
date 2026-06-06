text=str(input("Enter a text: "))
count=0
for i in text:
    if i in "aeiouAEIOU":
        count+=1
print("Number of vowels:", count)
