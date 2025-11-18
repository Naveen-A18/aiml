#a spam comment is defined as atext containing following keywords:
#"make a lot of money","buy now","subscribe this","click this",write a program to detect these spams
text = input("Enter the text: ").lower()
if "make a lot of money":
    print("This is a spam comment")
elif "buy now":
    print("This is a spam comment")
elif "subscribe this":
    print("This is a spam comment")
elif "click this":
    print("This is a spam comment")
else:
    print("This is not a spam comment")

