percent=float(input("Enter percentage of the student: "))
if percent>100:
    print("Invalid input")
elif percent>70:
    print("The student secured O grade.")    
elif percent>60:
    print("The student secured A grade.")
elif percent>40:
    print("The student secured B grade.")

else:
    print("The student failed.")
